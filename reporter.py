import json
import os
from datetime import datetime


def write_json_report(data: dict, name_prefix: str = "illumio_report") -> str:
    """
    Writes a JSON report into /out with a timestamped filename.
    Returns the output file path.
    """
    os.makedirs("out", exist_ok=True)

    filename = f"{name_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    path = os.path.join("out", filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return path
