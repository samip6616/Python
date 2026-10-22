/**
 * example_app.ts
 * Demonstrates using the LoggerFactory with structured logs and rotation-enabled FileLogger.
 *
 * Usage:
 *   ts-node example_app.ts file   # use file logger
 *   ts-node example_app.ts console
 *
 * You can also set rotation via environment variables or pass directly into LoggerFactory.
 */

import { LoggerFactory } from "./logger";

const mode = process.argv[2] ?? process.env.LOGGER_KIND ?? "console";

function main() {
  let logger;
  if (mode === "file") {
    logger = LoggerFactory.getLogger({
      kind: "file",
      filepath: "./logs/app.log",
      maxSizeBytes: 1024 * 10, // 10 KB for demo (small so rotation triggers quickly)
      maxFiles: 3,
      name: "app-file-logger",
    });
  } else if (mode === "noop") {
    logger = LoggerFactory.getLogger({ kind: "noop" });
  } else {
    logger = LoggerFactory.getLogger({ kind: "console" });
  }

  logger.info("Application starting", { env: process.env.NODE_ENV ?? "development" });

  for (let i = 0; i < 500; i++) {
    // create moderately sized messages so rotation will happen within loop
    logger.debug(`Processing item ${i}`, { itemIndex: i, payloadSize: 128 });
    if (i % 50 === 0) {
      logger.info("Checkpoint reached", { checkpoint: i });
    }
  }

  logger.info("Application finished");
}

main();