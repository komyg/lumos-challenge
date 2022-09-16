import pytest

from .. import error


def test_create_user():
    result = error.create_error("My error message")
    assert result == {"error": "My error message"}
