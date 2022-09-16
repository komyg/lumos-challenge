import pytest

from .. import identifier


def test_create_id_dict():
    result = identifier.create_id_dict(1)
    assert result == {"id": 1}
