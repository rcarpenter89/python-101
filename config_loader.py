import os
import yaml


def load_config(path: str) -> dict:
    """
    Loads YAML config file into a Python dictionary.
    Keeps it intentionally simple for Python 101.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        raise ValueError("Config file must contain a YAML dictionary at the root level.")

    # Basic required keys (simple validation)
    for key in ["base_url", "org_id"]:
        if key not in data or not data[key]:
            raise KeyError(f"Missing required config key: {key}")

    # Defaults
    data.setdefault("verify_ssl", True)
    data.setdefault("timeout_seconds", 30)

    # Normalize
    data["base_url"] = str(data["base_url"]).rstrip("/")
    data["org_id"] = int(data["org_id"])
    data["verify_ssl"] = bool(data["verify_ssl"])
    data["timeout_seconds"] = int(data["timeout_seconds"])

    return data
