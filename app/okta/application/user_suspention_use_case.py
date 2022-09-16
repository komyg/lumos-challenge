from app.okta.infrastructure.okta_client import client


def suspend_user(user_id):
    client.suspend_user(user_id)


def unsuspend_user(user_id):
    client.unsuspend_user(user_id)
