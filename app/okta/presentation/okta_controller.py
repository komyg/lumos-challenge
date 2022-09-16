from flask import request

from app.okta.application.list_users_use_case import list_users as list_users_use_case


def list_users():
    query_params = request.args
    return list_users_use_case(query_params)
