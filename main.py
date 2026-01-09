import os
import requests
from requests.auth import HTTPBasicAuth

from config import load_config


def main():
    config = load_config()

    base_url = config["base_url"]
    org_id = config["org_id"]

    api_user = os.getenv("ILLUMIO_API_USER")
    api_key = os.getenv("ILLUMIO_API_KEY")

    if not api_user or not api_key:
        print("Missing API credentials")
        return

    url = f"{base_url}/api/v2/orgs/{org_id}"

    response = requests.get(
        url,
        auth=HTTPBasicAuth(api_user, api_key),
        verify=config.get("verify_ssl", True),
    )

    print("Status code:", response.status_code)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
