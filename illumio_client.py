import requests
from requests.auth import HTTPBasicAuth


def make_session(api_user: str, api_key: str, user_agent: str = "illumio-python101/1.0") -> requests.Session:
    """
    Creates a requests Session with Basic Auth + default headers.
    """
    session = requests.Session()
    session.auth = HTTPBasicAuth(api_user, api_key)
    session.headers.update(
        {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": user_agent,
        }
    )
    return session


def test_connection(session: requests.Session, base_url: str, org_id: int, verify_ssl: bool, timeout_seconds: int) -> dict:
    """
    Simple auth/connectivity test call.

    NOTE: If your PCE doesn't support GET /api/v2/orgs/{org_id},
    swap this endpoint to one you know works in your environment.
    """
    url = f"{base_url}/api/v2/orgs/{org_id}"
    resp = session.get(url, verify=verify_ssl, timeout=timeout_seconds)

    if resp.status_code >= 400:
        raise RuntimeError(f"test_connection failed: HTTP {resp.status_code} - {resp.text}")

    return resp.json()


def get_workloads(session: requests.Session, base_url: str, org_id: int, verify_ssl: bool, timeout_seconds: int, limit: int = 10) -> list:
    """
    Example “real data” call: get workloads (limited).
    """
    url = f"{base_url}/api/v2/orgs/{org_id}/workloads"
    params = {"max_results": limit}

    resp = session.get(url, params=params, verify=verify_ssl, timeout=timeout_seconds)

    if resp.status_code >= 400:
        raise RuntimeError(f"get_workloads failed: HTTP {resp.status_code} - {resp.text}")

    data = resp.json()
    # Illumio responses can be list or object depending on endpoint/version; handle safely:
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "items" in data and isinstance(data["items"], list):
        return data["items"]

    # Fallback: return whatever we got in a list so the report still works
    return [data]
