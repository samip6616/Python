from abc import ABC, abstractmethod
from datetime import datetime
import sqlite3
from typing import List, Optional


class Logger(ABC):
    @abstractmethod
    def log(self, level: str, message: str) -> None:
        """Write a log entry at the specified level."""
        pass


class ConsoleLogger(Logger):
    def log(self, level: str, message: str) -> None:
        timestamp = datetime.utcnow().isoformat()
        print(f"{timestamp} [{level}] {message}")


class FileLogger(Logger):
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def log(self, level: str, message: str) -> None:
        timestamp = datetime.utcnow().isoformat()
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} [{level}] {message}\n")


class DatabaseLogger(Logger):
    def __init__(self, db_path: str = ":memory:") -> None:
        self.db_path = db_path
        self._conn = sqlite3.connect(self.db_path)
        self._ensure_table()

    def _ensure_table(self) -> None:
        cur = self._conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                level TEXT NOT NULL,
                message TEXT NOT NULL
            )
            """
        )
        self._conn.commit()

    def log(self, level: str, message: str) -> None:
        timestamp = datetime.utcnow().isoformat()
        cur = self._conn.cursor()
        cur.execute(
            "INSERT INTO logs (timestamp, level, message) VALUES (?, ?, ?)",
            (timestamp, level, message),
        )
        self._conn.commit()

    def fetch_all(self) -> List[sqlite3.Row]:
        cur = self._conn.cursor()
        cur.execute("SELECT id, timestamp, level, message FROM logs ORDER BY id")
        return cur.fetchall()


class MockLogger(Logger):
    """Useful for unit tests: collects messages in memory."""
    def __init__(self) -> None:
        self.records: List[tuple] = []

    def log(self, level: str, message: str) -> None:
        self.records.append((datetime.utcnow().isoformat(), level, message))

    def get_records(self) -> List[tuple]:
        return self.records[:]


class LoggerFactory:
    """Factory that returns concrete Logger instances based on a key."""

    @staticmethod
    def get_logger(kind: str, *, filepath: Optional[str] = None, db_path: Optional[str] = None) -> Logger:
        kind = kind.lower()
        if kind == "console":
            return ConsoleLogger()
        if kind == "file":
            if not filepath:
                raise ValueError("filepath is required for FileLogger")
            return FileLogger(filepath)
        if kind == "database" or kind == "db":
            return DatabaseLogger(db_path or ":memory:")
        if kind == "mock":
            return MockLogger()
        raise ValueError(f"Unknown logger kind: {kind}")
