"""
ConfigManager: Singleton configuration manager (JSON) with thread-safety and demo.

Usage:
    - First creation must provide the config file path.
    - Subsequent creations return the same instance.
    - Use .get("a.b.c", default) to fetch nested values by dotted path.
    - Call .reload() to force re-reading the file.

This file contains a small demo when executed as __main__.
"""
import json
import threading
from typing import Any, Optional


class SingletonMeta(type):
    """
    Thread-safe Singleton metaclass. Ensures only one instance is created.
    """
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # Double-checked locking
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class ConfigManager(metaclass=SingletonMeta):
    """
    Configuration manager singleton.
    - Reads a JSON config file once (unless reload() is called).
    - Provides get(key_path, default) for nested keys using dot notation.
    """
    # For demonstration purposes, track how many times the file was read.
    _read_count = 0

    def __init__(self, file_path: Optional[str] = None):
        """
        Initialize the config manager. The file_path is required the first time.
        Subsequent calls ignore file_path (or you may call reload()).
        """
        # Guard to ensure initialization code only runs once per instance.
        if getattr(self, "_initialized", False):
            # If different path provided after initialization, warn/ignore.
            if file_path and file_path != self._file_path:
                # We choose to ignore and keep the original config; alternatively we could raise.
                print(f"ConfigManager already initialized with '{self._file_path}'. Ignoring new path '{file_path}'.")
            return

        if not file_path:
            raise ValueError("First initialization requires a file_path to the configuration JSON file.")

        self._file_path = file_path
        self._config = {}
        self._config_lock = threading.RLock()  # protect reads/reloads
        self._load_from_file()
        self._initialized = True

    def _load_from_file(self):
        """
        Internal: read JSON file and cache it. Protected by _config_lock when public calls use it.
        """
        with self._config_lock:
            try:
                with open(self._file_path, "r", encoding="utf-8") as f:
                    self._config = json.load(f)
                type(self)._read_count += 1
                print(f"[ConfigManager] Loaded configuration from '{self._file_path}'. (read_count={self._read_count})")
            except FileNotFoundError as ex:
                raise FileNotFoundError(f"Configuration file not found: {self._file_path}") from ex
            except json.JSONDecodeError as ex:
                raise ValueError(f"Configuration file contains invalid JSON: {self._file_path}") from ex

    def get(self, key_path: str, default: Any = None) -> Any:
        """
        Get a configuration value using dotted path, e.g., "database.host".
        Returns default if key not present.
        """
        with self._config_lock:
            if not key_path:
                return default
            parts = key_path.split(".")
            node = self._config
            for part in parts:
                if isinstance(node, dict) and part in node:
                    node = node[part]
                else:
                    return default
            return node

    def reload(self) -> None:
        """
        Force re-reading the configuration file. Useful for runtime changes.
        """
        self._load_from_file()

    @classmethod
    def read_count(cls) -> int:
        """Return how many times the config file has been read (for demo/verification)."""
        return cls._read_count


# Demo code showing singleton behavior and thread-safety
if __name__ == "__main__":
    import os
    import time

    demo_path = "demo_config.json"
    demo_content = {
        "app": {"name": "MyApp", "version": "1.0.0"},
        "database": {"host": "localhost", "port": 5432},
        "features": {"enable_feature_x": True}
    }

    # Write demo config file
    with open(demo_path, "w", encoding="utf-8") as df:
        json.dump(demo_content, df, indent=2)

    print("Demo: Creating first ConfigManager instance (must pass file path).")
    cfg1 = ConfigManager(demo_path)
    print("cfg1 id:", id(cfg1))
    print("app.name:", cfg1.get("app.name"))
    print("database.port:", cfg1.get("database.port"))
    print("missing.key (with default):", cfg1.get("no.such.key", "default-value"))
    print("Read count after first init:", ConfigManager.read_count())

    print("\nDemo: Creating second ConfigManager instance (no file path provided).")
    cfg2 = ConfigManager()  # should return the same instance
    print("cfg2 id:", id(cfg2))
    print("cfg1 is cfg2:", cfg1 is cfg2)
    print("Read count after second init:", ConfigManager.read_count())

    print("\nDemo: Attempt to create with a different path (ignored).")
    other_path = "other_config.json"
    # create a different file name but we'll ignore it
    with open(other_path, "w", encoding="utf-8") as df:
        json.dump({"app": {"name": "OtherApp"}}, df)
    cfg3 = ConfigManager(other_path)
    print("cfg3 id:", id(cfg3))
    print("cfg1 is cfg3:", cfg1 is cfg3)
    print("Read count after ignored init:", ConfigManager.read_count())

    # Multithreaded creation attempt
    print("\nDemo: Multithreaded creation attempts to test thread-safety.")
    created_instances = []
    def make_instance():
        inst = ConfigManager(demo_path)
        created_instances.append(id(inst))

    threads = [threading.Thread(target=make_instance) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Unique instance ids created by threads:", sorted(set(created_instances)))
    print("Read count after multithreaded attempts:", ConfigManager.read_count())

    # Demonstrate reload
    print("\nDemo: Modify config file and call reload().")
    demo_content["app"]["version"] = "2.0.0"
    with open(demo_path, "w", encoding="utf-8") as df:
        json.dump(demo_content, df, indent=2)

    print("Before reload - app.version:", cfg1.get("app.version"))
    cfg1.reload()
    print("After reload  - app.version:", cfg1.get("app.version"))
    print("Read count after reload:", ConfigManager.read_count())

    # Clean up demo files
    try:
        os.remove(demo_path)
        os.remove(other_path)
    except OSError:
        pass