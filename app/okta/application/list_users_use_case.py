from app.okta.infrastructure.okta_client import client
from app.okta.domain.user import create_user


def list_users(query_params=None) -> dict[str, any]:
    okta_user_list = client.list_users(query_params)
    return list(map(lambda okta_user: create_user(okta_user), okta_user_list))
