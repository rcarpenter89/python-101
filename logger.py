import logging
import os
from datetime import datetime


def setup_logging() -> str:
    os.makedirs("logs", exist_ok=True)

    log_file = os.path.join(
        "logs", f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    )

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )

    logging.info("Logging initialized")
    return log_file
