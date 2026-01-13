import logging
import os
import sys

from logger_setup import setup_logging
from config_loader import load_config
from reporter import write_json_report
from illumio_client import make_session, test_connection, get_workloads


DEFAULT_CONFIG_PATH = "config/settings.yaml"


def get_env_or_fail(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing environment variable: {name}")
    return value


def main() -> int:
    setup_logging()

    # Keep the run simple: config path optional via CLI arg #1
    config_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CONFIG_PATH
    logging.info(f"Using config file: {config_path}")

    try:
        cfg = load_config(config_path)

        # Compliant auth: secrets from environment variables
        # (Do NOT log these values.)
        api_user = get_env_or_fail("ILLUMIO_API_USER")
        api_key = get_env_or_fail("ILLUMIO_API_KEY")

        session = make_session(api_user, api_key)

        logging.info("Testing Illumio connection (Basic Auth)...")
        org_info = test_connection(
            session=session,
            base_url=cfg["base_url"],
            org_id=cfg["org_id"],
            verify_ssl=cfg["verify_ssl"],
            timeout_seconds=cfg["timeout_seconds"],
        )
        logging.info("Connection test succeeded.")

        logging.info("Fetching a small workload sample...")
        workloads = get_workloads(
            session=session,
            base_url=cfg["base_url"],
            org_id=cfg["org_id"],
            verify_ssl=cfg["verify_ssl"],
            timeout_seconds=cfg["timeout_seconds"],
            limit=10,
        )
        logging.info(f"Workloads returned: {len(workloads)}")

        report = {
            "config_used": {
                "base_url": cfg["base_url"],
                "org_id": cfg["org_id"],
                "verify_ssl": cfg["verify_ssl"],
                "timeout_seconds": cfg["timeout_seconds"],
            },
            "org_info": org_info,
            "workloads_sample_count": len(workloads),
            "workloads_sample": workloads,
        }

        out_path = write_json_report(report, name_prefix="illumio_training")
        logging.info(f"Report written: {out_path}")

        print("\n=== RUN SUMMARY ===")
        print("Status: SUCCESS")
        print(f"Workloads returned: {len(workloads)}")
        print(f"Report: {out_path}")
        print("===================\n")

        return 0

    except FileNotFoundError as e:
        logging.error(f"Config file not found: {e}")
    except KeyError as e:
        logging.error(f"Config missing required key: {e}")
    except ValueError as e:
        logging.error(f"Configuration/auth error: {e}")
    except Exception as e:
        logging.exception(f"Unexpected error: {e}")

    print("\nStatus: FAILED (check logs/ for details)\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
