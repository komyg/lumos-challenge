from flask import Flask
from dotenv import load_dotenv

from .okta.presentation import okta_routes
from .common.infrastructure.environment_config import PORT, DEBUG

load_dotenv()

app = Flask(__name__)

app.register_blueprint(okta_routes.okta_blueprint)

if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)
