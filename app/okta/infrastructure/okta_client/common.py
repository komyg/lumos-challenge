from app.common.infrastructure.environment_config import OKTA_TOKEN, OKTA_URL


def get_base_headers():
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"SSWS {OKTA_TOKEN}",
    }


def get_base_url():
    return OKTA_URL
