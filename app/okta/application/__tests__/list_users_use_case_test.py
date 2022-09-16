import pytest
from unittest.mock import patch
from returns.result import Success, Failure

from .. import list_users_use_case


@patch("app.okta.application.list_users_use_case.client", spec=True)
@patch("app.okta.application.list_users_use_case.create_user", spec=True)
def test_list_users_success(create_user_mock, client_mock):
    client_mock.list_users.return_value = Success(
        [
            {"id": 1, "hello": "world"},
            {"id": 2, "hello": "world"},
        ]
    )
    create_user_mock.return_value = {"hello": "world"}

    result = list_users_use_case.list_users()

    assert result.unwrap() == [{"hello": "world"}, {"hello": "world"}]


@patch("app.okta.application.list_users_use_case.client", spec=True)
@patch("app.okta.application.list_users_use_case.create_user", spec=True)
def test_list_users_failure(create_user_mock, client_mock):
    client_mock.list_users.return_value = Failure("My error")
    create_user_mock.return_value = {"hello": "world"}

    result = list_users_use_case.list_users()

    assert result.failure() == {"error": "My error"}
