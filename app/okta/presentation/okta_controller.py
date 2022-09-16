from flask import request
from returns.pipeline import is_successful
from returns.result import Result

from app.okta.application.list_users_use_case import list_users as list_users_use_case
from app.okta.application import user_suspention_use_case as user_suspention


def list_users():
    query_params = request.args
    result = list_users_use_case(query_params)
    return _process_response(result)


def suspend_user(user_id):
    result = user_suspention.suspend_user(user_id)
    return _process_response(result)


def unsuspend_user(user_id):
    result = user_suspention.unsuspend_user(user_id)
    return _process_response(result)


def _process_response(result: Result[dict[str, any], dict[str, str]]):
    if not is_successful(result):
        return result.failure(), 400

    return result.unwrap()
