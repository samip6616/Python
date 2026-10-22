from Factory_Design_Logger import LoggerFactory, Logger
import sys


def do_work(logger: Logger) -> None:
    logger.log("INFO", "Starting work")
    try:
        # Simulated work
        x = 1 / 1  # change to 1/0 to simulate an error
        logger.log("DEBUG", f"Intermediate result: {x}")
    except Exception as exc:
        logger.log("ERROR", f"Work failed: {exc}")
    else:
        logger.log("INFO", "Work finished successfully")


def main(argv):
    # Choose logger type via command-line argument or default to console
    kind = argv[1] if len(argv) > 1 else "console"

    if kind == "file":
        logger = LoggerFactory.get_logger("file", filepath="app.log")
    elif kind in ("db", "database"):
        logger = LoggerFactory.get_logger("database", db_path="app_logs.db")
    else:
        logger = LoggerFactory.get_logger(kind)

    do_work(logger)

    # Example of reading back DB logs (only if we used DatabaseLogger)
    if kind in ("db", "database"):
        # type-checker: this cast is safe because we asked for DatabaseLogger
        db_logger = logger  # type: ignore
        print("Logs stored in database.")


if __name__ == "__main__":
    main(sys.argv)