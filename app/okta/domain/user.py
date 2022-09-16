USER_FIELDS = {
    "id",
    "status",
    "created",
    "activated",
    "statusChanged",
    "lastLogin",
    "lastUpdated",
    "passwordChanged",
    "profile",
}


def create_user(okta_user: dict[str, any]) -> dict[str, any]:
    user = {}

    for key, value in okta_user.items():
        if key in USER_FIELDS:
            user[key] = value

    return user
