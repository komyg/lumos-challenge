import pytest
from unittest.mock import patch
from returns.result import Success, Failure

from .. import user_suspention_use_case


@patch("app.okta.application.user_suspention_use_case.client", spec=True)
def test_suspend_user_success(client_mock):
    client_mock.suspend_user.return_value = Success("1")

    result = user_suspention_use_case.suspend_user("1")
    assert result.unwrap() == {"id": "1"}


@patch("app.okta.application.user_suspention_use_case.client", spec=True)
def test_suspend_user_failure(client_mock):
    client_mock.suspend_user.return_value = Failure("My error")

    result = user_suspention_use_case.suspend_user("1")
    assert result.failure() == {"error": "My error"}


@patch("app.okta.application.user_suspention_use_case.client", spec=True)
def test_unsuspend_user_success(client_mock):
    client_mock.unsuspend_user.return_value = Success("1")

    result = user_suspention_use_case.unsuspend_user("1")
    assert result.unwrap() == {"id": "1"}


@patch("app.okta.application.user_suspention_use_case.client", spec=True)
def test_unsuspend_user_failure(client_mock):
    client_mock.unsuspend_user.return_value = Failure("My error")

    result = user_suspention_use_case.unsuspend_user("1")
    assert result.failure() == {"error": "My error"}
