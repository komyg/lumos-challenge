import requests
from returns.result import Result, Success, Failure

from .common import get_base_headers, get_base_url, parse_error


def list_users(query_params: str) -> Result[dict[str, any], str]:
    url = f"{get_base_url()}/api/v1/users"

    resp = requests.get(url=url, params=query_params, headers=get_base_headers())
    data = resp.json()

    return Success(data) if resp.status_code < 400 else Failure(parse_error(data))


def suspend_user(user_id: str):
    url = f"{get_base_url()}/api/v1/users/{user_id}/lifecycle/suspend"
    resp = requests.post(url=url, headers=get_base_headers())

    return (
        Success(user_id)
        if resp.status_code < 400
        else Failure(parse_error(resp.json()))
    )


def unsuspend_user(user_id: str):
    url = f"{get_base_url()}/api/v1/users/{user_id}/lifecycle/unsuspend"
    resp = requests.post(url=url, headers=get_base_headers())

    return (
        Success(user_id)
        if resp.status_code < 400
        else Failure(parse_error(resp.json()))
    )


def delete_user(user_id: str):
    url = f"{get_base_url()}/api/v1/users/{user_id}"
    resp = requests.delete(url=url, headers=get_base_headers())

    return (
        Success(user_id)
        if resp.status_code < 400
        else Failure(parse_error(resp.json()))
    )
