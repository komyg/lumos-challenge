import pytest

from .. import user


def test_create_user(okta_user):
    result = user.create_user(okta_user)
    print(result)
    for key in result.keys():
        assert key in user.USER_FIELDS


@pytest.fixture
def okta_user():
    return {
        "id": "00u6i89ld1pczME8i5d7",
        "status": "STAGED",
        "created": "2022-09-14T19:11:24.000Z",
        "activated": None,
        "statusChanged": None,
        "lastLogin": None,
        "lastUpdated": "2022-09-14T19:11:24.000Z",
        "passwordChanged": None,
        "type": {"id": "oty6i3814rTwQsKeT5d7"},
        "profile": {
            "firstName": "Jane",
            "lastName": "Doe",
            "mobilePhone": None,
            "secondEmail": None,
            "login": "1sm8cbhr@duck.com",
            "email": "1sm8cbhr@duck.com",
        },
        "credentials": {
            "emails": [
                {
                    "value": "1sm8cbhr@duck.com",
                    "status": "VERIFIED",
                    "type": "PRIMARY",
                }
            ],
            "provider": {"type": "OKTA", "name": "OKTA"},
        },
        "_links": {
            "self": {
                "href": "https://dev-20578441.okta.com/api/v1/users/00u6i89ld1pczME8i5d7"
            }
        },
    }
