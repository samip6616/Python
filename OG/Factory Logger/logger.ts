/**
 * logger.ts
 * - ILogger interface (structured logs)
 * - ConsoleLogger (structured JSON to stdout)
 * - FileLogger (structured JSON lines + size-based rotation)
 * - NoopLogger (useful for tests)
 * - LoggerFactory
 */

import * as fs from "fs";
import * as path from "path";
import * as os from "os";

export type LogLevel = "debug" | "info" | "warn" | "error";

export interface LogMeta {
  [key: string]: unknown;
}

export interface LogEntry {
  timestamp: string; // ISO 8601
  level: LogLevel;
  message: string;
  meta?: LogMeta;
  pid?: number;
  hostname?: string;
  logger?: string;
}

export interface ILogger {
  log(level: LogLevel, message: string, meta?: LogMeta): void;
  debug(message: string, meta?: LogMeta): void;
  info(message: string, meta?: LogMeta): void;
  warn(message: string, meta?: LogMeta): void;
  error(message: string, meta?: LogMeta): void;
}

/* ----------------------------- Helpers ----------------------------- */

function makeEntry(level: LogLevel, message: string, meta?: LogMeta, loggerName?: string): LogEntry {
  return {
    timestamp: new Date().toISOString(),
    level,
    message,
    meta,
    pid: process.pid,
    hostname: os.hostname(),
    logger: loggerName,
  };
}

/* --------------------------- ConsoleLogger ------------------------- */

export class ConsoleLogger implements ILogger {
  private name: string;
  constructor(name = "console") {
    this.name = name;
  }

  log(level: LogLevel, message: string, meta?: LogMeta): void {
    const entry = makeEntry(level, message, meta, this.name);
    // Structured JSON line to stdout (one JSON object per line)
    // Use console.log so output integrates with testing/containers
    console.log(JSON.stringify(entry));
  }
  debug(message: string, meta?: LogMeta): void { this.log("debug", message, meta); }
  info(message: string, meta?: LogMeta): void { this.log("info", message, meta); }
  warn(message: string, meta?: LogMeta): void { this.log("warn", message, meta); }
  error(message: string, meta?: LogMeta): void { this.log("error", message, meta); }
}

/* ---------------------------- FileLogger -------------------------- */

/**
 * FileLogger writes newline-delimited JSON logs to a file.
 * It supports size-based rotation:
 * - When the current file exceeds `maxSizeBytes`, rotate:
 *   app.log -> app.log.1, app.log.1 -> app.log.2, ... up to maxFiles.
 * - Keep up to `maxFiles` backups; if maxFiles === 0 the logger truncates the file on rotation.
 *
 * Note: This implementation uses synchronous file ops for rotation correctness and simplicity.
 * For very high-throughput systems prefer a write-stream + async rotation approach.
 */

export interface FileLoggerOptions {
  filepath: string;
  maxSizeBytes?: number; // default: 5 MB
  maxFiles?: number;     // default: 5
  name?: string;         // optional logger name included in each entry
}

export class FileLogger implements ILogger {
  private filepath: string;
  private maxSizeBytes: number;
  private maxFiles: number;
  private bytesWritten: number;
  private name: string;

  constructor(opts: FileLoggerOptions) {
    this.filepath = path.resolve(opts.filepath);
    this.maxSizeBytes = opts.maxSizeBytes ?? 5 * 1024 * 1024; // 5 MB default
    this.maxFiles = typeof opts.maxFiles === "number" ? Math.max(0, Math.floor(opts.maxFiles)) : 5;
    this.name = opts.name ?? "file";

    // Ensure directory exists
    const dir = path.dirname(this.filepath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    this.bytesWritten = 0;
    if (fs.existsSync(this.filepath)) {
      try {
        const st = fs.statSync(this.filepath);
        this.bytesWritten = st.size;
      } catch {
        this.bytesWritten = 0;
      }
    } else {
      // ensure file exists
      fs.closeSync(fs.openSync(this.filepath, "a"));
      this.bytesWritten = 0;
    }
  }

  private rotateIfNeeded(additionalBytes = 0): void {
    if (this.maxSizeBytes <= 0) return; // no rotation if set to 0 or negative
    if (this.bytesWritten + additionalBytes < this.maxSizeBytes) return;

    // Perform rotation
    // Delete / shift backups: file -> file.1, file.1 -> file.2, ... (highest dropped)
    if (this.maxFiles > 0) {
      // Remove oldest if exists
      const oldest = `${this.filepath}.${this.maxFiles}`;
      if (fs.existsSync(oldest)) {
        try { fs.unlinkSync(oldest); } catch { /* ignore */ }
      }
      // Shift backups up
      for (let i = this.maxFiles - 1; i >= 1; i--) {
        const from = `${this.filepath}.${i}`;
        const to = `${this.filepath}.${i + 1}`;
        if (fs.existsSync(from)) {
          try { fs.renameSync(from, to); } catch {/* ignore */ }
        }
      }
      // Move current file to .1
      try {
        if (fs.existsSync(this.filepath)) {
          fs.renameSync(this.filepath, `${this.filepath}.1`);
        }
      } catch (err) {
        // If rename fails, fallback to truncation
        try { fs.truncateSync(this.filepath, 0); } catch { /* ignore */ }
      }
    } else {
      // maxFiles === 0 -> we will truncate current file
      try { fs.truncateSync(this.filepath, 0); } catch { /* ignore */ }
    }

    // Recreate an empty base file if missing
    try {
      fs.closeSync(fs.openSync(this.filepath, "a"));
    } catch {/* ignore */ }

    // reset counter
    this.bytesWritten = 0;
  }

  log(level: LogLevel, message: string, meta?: LogMeta): void {
    const entry = makeEntry(level, message, meta, this.name);
    const line = JSON.stringify(entry) + os.EOL;
    const byteCount = Buffer.byteLength(line, "utf8");

    // rotate if needed BEFORE writing, so the new entry starts in a new file when threshold passed
    this.rotateIfNeeded(byteCount);

    // write synchronously for simplicity/robustness
    try {
      fs.appendFileSync(this.filepath, line, { encoding: "utf8" });
      this.bytesWritten += byteCount;
    } catch (err) {
      // If file writing fails, fallback to console for reliability
      // (We still want to expose structured logs)
      // Avoid throwing to keep logging non-fatal
      console.error(JSON.stringify({
        timestamp: new Date().toISOString(),
        level: "error",
        message: "FileLogger write failed, falling back to console",
        error: (err as Error).message,
        attemptedEntry: entry,
      }));
    }
  }

  debug(message: string, meta?: LogMeta): void { this.log("debug", message, meta); }
  info(message: string, meta?: LogMeta): void { this.log("info", message, meta); }
  warn(message: string, meta?: LogMeta): void { this.log("warn", message, meta); }
  error(message: string, meta?: LogMeta): void { this.log("error", message, meta); }
}

/* ---------------------------- NoopLogger --------------------------- */

export class NoopLogger implements ILogger {
  log(_level: LogLevel, _message: string, _meta?: LogMeta): void { /* noop */ }
  debug(_message: string, _meta?: LogMeta): void { /* noop */ }
  info(_message: string, _meta?: LogMeta): void { /* noop */ }
  warn(_message: string, _meta?: LogMeta): void { /* noop */ }
  error(_message: string, _meta?: LogMeta): void { /* noop */ }
}

/* --------------------------- LoggerFactory ------------------------ */

export type LoggerKind = "console" | "file" | "noop";

export interface LoggerFactoryOptions {
  kind: LoggerKind;
  // File logger specific
  filepath?: string;
  maxSizeBytes?: number;
  maxFiles?: number;
  name?: string;
}

export class LoggerFactory {
  static getLogger(opts: LoggerFactoryOptions): ILogger {
    const kind = opts.kind;
    switch (kind) {
      case "console":
        return new ConsoleLogger(opts.name);
      case "file":
        if (!opts.filepath) {
          throw new Error("LoggerFactory: filepath is required for file logger");
        }
        return new FileLogger({
          filepath: opts.filepath,
          maxSizeBytes: opts.maxSizeBytes,
          maxFiles: opts.maxFiles,
          name: opts.name,
        });
      case "noop":
        return new NoopLogger();
      default:
        throw new Error(`LoggerFactory: unknown logger kind: ${String(kind)}`);
    }
  }
}