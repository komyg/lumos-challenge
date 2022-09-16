import requests

from .common import get_base_headers, get_base_url


def list_users(query_params: str):
    url = f"{get_base_url()}/api/v1/users"

    resp = requests.get(url=url, params=query_params, headers=get_base_headers())
    return resp.json()
