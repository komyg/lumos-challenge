from dotenv import dotenv_values

config = dotenv_values(".env")

PORT = config.get("PORT") or 5000
DEBUG = config.get("DEBUG") == "true"
OKTA_URL = config.get("OKTA_URL") or ""
OKTA_TOKEN = config.get("OKTA_TOKEN") or ""
