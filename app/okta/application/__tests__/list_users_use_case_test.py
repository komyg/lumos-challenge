import pytest
from unittest.mock import patch

from .. import list_users_use_case


@patch("app.okta.application.list_users_use_case.client", spec=True)
@patch("app.okta.application.list_users_use_case.create_user", spec=True)
def test_list_users(create_user_mock, client_mock):
    client_mock.list_users.return_value = [
        {"id": 1, "hello": "world"},
        {"id": 2, "hello": "world"},
    ]
    create_user_mock.return_value = {"hello": "world"}

    result = list_users_use_case.list_users()

    assert result == [{"hello": "world"}, {"hello": "world"}]
