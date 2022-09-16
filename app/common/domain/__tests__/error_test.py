import pytest

from .. import error


def test_create_error_dict():
    result = error.create_error_dict("My error message")
    assert result == {"error": "My error message"}
