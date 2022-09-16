import pytest
from unittest.mock import patch
from returns.result import Success, Failure

from .. import user_deletion_use_case


@patch("app.okta.application.user_deletion_use_case.client", spec=True)
def test_delete_user_success(client_mock):
    client_mock.delete_user.return_value = Success("1")

    result = user_deletion_use_case.delete_user("1")
    assert result.unwrap() == {"id": "1"}


@patch("app.okta.application.user_deletion_use_case.client", spec=True)
def test_delete_user_error(client_mock):
    client_mock.delete_user.return_value = Failure("My error")

    result = user_deletion_use_case.delete_user("1")
    assert result.failure() == {"error": "My error"}
