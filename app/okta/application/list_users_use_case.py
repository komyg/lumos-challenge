from app.okta.infrastructure.okta_client import client


def list_users(query_params=None):
    return client.list_users(query_params)
