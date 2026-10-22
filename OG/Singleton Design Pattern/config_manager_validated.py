"""
ConfigManager with Singleton, typed accessors, and JSON Schema validation.

Features:
- Thread-safe Singleton (metaclass).
- Load config from JSON file once (cached); reload() to re-read.
- Optional JSON Schema (dict or file path) used to validate config on load/reload.
- Typed accessors: get_str, get_int, get_bool, get_float, get_list, get_dict.
- map_to_dataclass(section_path, dataclass_type) helper to instantiate dataclass from config section.
- Demo shows successful validation, failing validation, typed accessors, reload, and dataclass mapping.

Dependencies:
    pip install jsonschema
"""
from __future__ import annotations
import json
import threading
from typing import Any, Optional, Iterable, Type, Dict
from dataclasses import dataclass, fields, is_dataclass
from jsonschema import Draft7Validator, validators, ValidationError
import os

# Singleton metaclass (thread-safe)
class SingletonMeta(type):
    _instances: Dict[type, object] = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


def _load_json_file(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


class ConfigManager(metaclass=SingletonMeta):
    """
    Configuration manager singleton with JSON Schema validation and typed accessors.

    Usage:
        cfg = ConfigManager(config_path, schema=...optional...)
        cfg.get_str("db.host")
        cfg.get_int("db.port", default=5432)
        cfg.map_to_dataclass("app", MyAppConfigDataclass)
        cfg.reload()
    """

    _read_count = 0

    def __init__(self, file_path: Optional[str] = None, schema: Optional[Any] = None):
        if getattr(self, "_initialized", False):
            # If user passed different file_path or schema after init we ignore them.
            if file_path and file_path != getattr(self, "_file_path", None):
                print(f"[ConfigManager] Already initialized with '{self._file_path}'. Ignoring new path '{file_path}'.")
            if schema and schema != getattr(self, "_schema", None):
                print("[ConfigManager] Schema already set on initial initialization; ignoring new schema argument.")
            return

        if not file_path:
            raise ValueError("First initialization requires a file_path to the configuration JSON file.")

        self._file_path = file_path
        self._config_lock = threading.RLock()
        self._config: dict = {}
        # Schema can be a dict or a path to schema file. Keep the raw schema as dict or None.
        self._schema = None
        if schema:
            if isinstance(schema, str):
                if not os.path.exists(schema):
                    raise FileNotFoundError(f"Schema file not found: {schema}")
                self._schema = _load_json_file(schema)
            elif isinstance(schema, dict):
                self._schema = schema
            else:
                raise TypeError("schema must be a dict or a path to a JSON schema file")

        # Prepare validator if schema provided
        self._validator = self._prepare_validator(self._schema) if self._schema else None

        # Load the config file (and validate if schema present)
        self._load_from_file()
        self._initialized = True

    @classmethod
    def _prepare_validator(cls, schema: dict) -> Draft7Validator:
        # Extend if needed. For now use Draft7Validator.
        return Draft7Validator(schema)

    def _load_from_file(self):
        with self._config_lock:
            try:
                self._config = _load_json_file(self._file_path)
                type(self)._read_count += 1
                print(f"[ConfigManager] Loaded configuration from '{self._file_path}'. (read_count={self._read_count})")
                if self._validator:
                    self._run_validation()
            except FileNotFoundError as ex:
                raise FileNotFoundError(f"Configuration file not found: {self._file_path}") from ex
            except json.JSONDecodeError as ex:
                raise ValueError(f"Configuration file contains invalid JSON: {self._file_path}") from ex

    def _run_validation(self) -> None:
        """
        Validate config against the schema. Raises jsonschema.ValidationError on failure.
        """
        assert self._validator is not None
        errors = sorted(self._validator.iter_errors(self._config), key=lambda e: e.path)
        if errors:
            # Format errors to a readable message
            messages = []
            for e in errors:
                path = ".".join(map(str, e.path)) if e.path else "<root>"
                messages.append(f"{path}: {e.message}")
            details = "\n".join(messages)
            raise ValidationError(f"Configuration validation failed:\n{details}")

    def validate(self) -> None:
        """
        Public method to run validation now. Raises ValidationError if invalid.
        """
        if not self._validator:
            raise RuntimeError("No schema provided for validation")
        with self._config_lock:
            self._run_validation()

    # --- Access helpers ---
    def _get_node(self, key_path: str) -> Any:
        if not key_path:
            return None
        parts = key_path.split(".")
        node = self._config
        for part in parts:
            if isinstance(node, dict) and part in node:
                node = node[part]
            else:
                return None
        return node

    def get(self, key_path: str, default: Any = None) -> Any:
        with self._config_lock:
            node = self._get_node(key_path)
            return node if node is not None else default

    def get_str(self, key_path: str, default: Optional[str] = None) -> Optional[str]:
        val = self.get(key_path, default)
        if val is None:
            return default
        if isinstance(val, str):
            return val
        # Try to convert
        return str(val)

    def get_int(self, key_path: str, default: Optional[int] = None) -> Optional[int]:
        val = self.get(key_path, default)
        if val is None:
            return default
        if isinstance(val, bool):
            # bool is subclass of int but usually not desired
            raise TypeError(f"Value at '{key_path}' is boolean, not integer.")
        if isinstance(val, int):
            return val
        try:
            return int(val)
        except (ValueError, TypeError):
            raise TypeError(f"Cannot convert value at '{key_path}' to int: {val!r}")

    def get_float(self, key_path: str, default: Optional[float] = None) -> Optional[float]:
        val = self.get(key_path, default)
        if val is None:
            return default
        if isinstance(val, (int, float)) and not isinstance(val, bool):
            return float(val)
        try:
            return float(val)
        except (ValueError, TypeError):
            raise TypeError(f"Cannot convert value at '{key_path}' to float: {val!r}")

    def get_bool(self, key_path: str, default: Optional[bool] = None) -> Optional[bool]:
        val = self.get(key_path, default)
        if val is None:
            return default
        if isinstance(val, bool):
            return val
        if isinstance(val, str):
            lowered = val.strip().lower()
            if lowered in ("true", "yes", "1", "on"):
                return True
            if lowered in ("false", "no", "0", "off"):
                return False
            raise TypeError(f"Cannot convert string to bool for '{key_path}': {val!r}")
        if isinstance(val, (int, float)):
            return bool(val)
        raise TypeError(f"Cannot convert value at '{key_path}' to bool: {val!r}")

    def get_list(self, key_path: str, default: Optional[Iterable] = None) -> Optional[list]:
        val = self.get(key_path, default)
        if val is None:
            return default
        if isinstance(val, list):
            return val
        raise TypeError(f"Value at '{key_path}' is not a list: {type(val).__name__}")

    def get_dict(self, key_path: str, default: Optional[dict] = None) -> Optional[dict]:
        val = self.get(key_path, default)
        if val is None:
            return default
        if isinstance(val, dict):
            return val
        raise TypeError(f"Value at '{key_path}' is not a dict: {type(val).__name__}")

    def map_to_dataclass(self, section_path: str, dataclass_type: Type[Any]) -> Any:
        """
        Map a dict at section_path to a dataclass instance.
        The dataclass fields must match the keys in the dict. Extra keys in the dict will be ignored.
        """
        if not is_dataclass(dataclass_type):
            raise TypeError("dataclass_type must be a dataclass type")

        section = self.get_dict(section_path, default=None)
        if section is None:
            raise KeyError(f"Configuration section '{section_path}' not found or is not an object")

        # Filter keys to those in dataclass fields
        field_names = {f.name for f in fields(dataclass_type)}
        filtered = {k: v for k, v in section.items() if k in field_names}
        try:
            return dataclass_type(**filtered)
        except TypeError as ex:
            raise TypeError(f"Failed to instantiate dataclass {dataclass_type.__name__}: {ex}") from ex

    def reload(self) -> None:
        """
        Force re-load of the configuration from disk. Re-validates against the schema if present.
        """
        self._load_from_file()

    @classmethod
    def read_count(cls) -> int:
        return cls._read_count


# -----------------------
# Demo usage
# -----------------------
if __name__ == "__main__":
    import tempfile
    from jsonschema import ValidationError as JsonValidationError

    demo_config = {
        "app": {"name": "ExampleApp", "version": "1.2.3"},
        "database": {"host": "db.example.local", "port": 3306, "use_ssl": False},
        "features": {"enable_x": True, "threshold": 0.75}
    }

    demo_schema = {
        "type": "object",
        "required": ["app", "database"],
        "properties": {
            "app": {
                "type": "object",
                "required": ["name", "version"],
                "properties": {
                    "name": {"type": "string"},
                    "version": {"type": "string", "pattern": r"^\d+\.\d+\.\d+$"}
                }
            },
            "database": {
                "type": "object",
                "required": ["host", "port"],
                "properties": {
                    "host": {"type": "string"},
                    "port": {"type": "integer", "minimum": 1, "maximum": 65535},
                    "use_ssl": {"type": "boolean"}
                }
            },
            "features": {
                "type": "object",
                "properties": {
                    "enable_x": {"type": "boolean"},
                    "threshold": {"type": "number", "minimum": 0.0, "maximum": 1.0}
                }
            }
        }
    }

    # Create temp files
    tmp_dir = tempfile.gettempdir()
    cfg_path = os.path.join(tmp_dir, "demo_config.json")
    schema_path = os.path.join(tmp_dir, "demo_schema.json")
    with open(cfg_path, "w", encoding="utf-8") as f:
        json.dump(demo_config, f, indent=2)
    with open(schema_path, "w", encoding="utf-8") as f:
        json.dump(demo_schema, f, indent=2)

    # Define a dataclass for the app section
    @dataclass
    class AppConfig:
        name: str
        version: str

    print("Demo: Initialize ConfigManager with schema (by dict).")
    cfg = ConfigManager(cfg_path, schema=demo_schema)
    print("Read count:", ConfigManager.read_count())

    # Typed accessors
    print("app.name (str)       :", cfg.get_str("app.name"))
    print("database.port (int)  :", cfg.get_int("database.port"))
    print("features.threshold(f):", cfg.get_float("features.threshold"))
    print("features.enable_x (b):", cfg.get_bool("features.enable_x"))

    # map to dataclass
    app_conf = cfg.map_to_dataclass("app", AppConfig)
    print("Dataclass mapping:", app_conf)

    # Demonstrate failed validation: change file to invalid port
    print("\nDemo: Writing invalid config to show validation errors on reload.")
    demo_config_invalid = dict(demo_config)
    demo_config_invalid["database"] = dict(demo_config_invalid["database"])
    demo_config_invalid["database"]["port"] = 70000  # invalid: > 65535
    with open(cfg_path, "w", encoding="utf-8") as f:
        json.dump(demo_config_invalid, f, indent=2)

    try:
        cfg.reload()
        print("Reloaded successfully (unexpected).")
    except JsonValidationError as ex:
        print("ValidationError on reload (expected):")
        print(str(ex))

    # Fix config and reload
    print("\nDemo: Fixing config and reloading.")
    with open(cfg_path, "w", encoding="utf-8") as f:
        json.dump(demo_config, f, indent=2)
    cfg.reload()
    print("Reloaded successfully.")
    print("database.port after fix:", cfg.get_int("database.port"))

    # Cleanup demo files
    try:
        os.remove(cfg_path)
        os.remove(schema_path)
    except OSError:
        pass