import requests

from .common import get_base_headers, get_base_url


def list_users(query_params: str) -> dict[str, any]:
    url = f"{get_base_url()}/api/v1/users"

    resp = requests.get(url=url, params=query_params, headers=get_base_headers())
    return resp.json()


def suspend_user(user_id: str) -> None:
    url = f"{get_base_url()}/api/v1/users/{user_id}/lifecycle/suspend"
    requests.post(url=url, headers=get_base_headers())


def unsuspend_user(user_id: str) -> None:
    url = f"{get_base_url()}/api/v1/users/{user_id}/lifecycle/unsuspend"
    requests.post(url=url, headers=get_base_headers())


def delete_user(user_id: str) -> None:
    url = f"{get_base_url()}/api/v1/users/{user_id}"
    requests.delete(url=url, headers=get_base_headers())
