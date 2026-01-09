import logging
from datetime import datetime
import os

def setup_logging():
    os.makedirs("logs", exist_ok=True)
    log_file = os.path.join("logs", f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging initialized")


def main():
    setup_logging()
    try:
        # existing logic here
        ...
    except FileNotFoundError as e:
        logging.error(f"Config file issue: {e}")
    except KeyError as e:
        logging.error(f"Missing required config key: {e}")
    except Exception as e:
        logging.exception(f"Unexpected error: {e}")

