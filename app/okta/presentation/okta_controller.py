from flask import request

from app.okta.application.list_users_use_case import list_users as list_users_use_case
from app.okta.application import user_suspention_use_case as user_suspention


def list_users():
    query_params = request.args
    return list_users_use_case(query_params)


def suspend_user(user_id):
    user_suspention.suspend_user(user_id)
    return {"ok": True}


def unsuspend_user(user_id):
    user_suspention.unsuspend_user(user_id)
    return {"ok": True}
