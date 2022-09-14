from flask import Flask

from .okta.presentation import okta_routes

app = Flask(__name__)

app.register_blueprint(okta_routes.okta_blueprint)
# API Token: 00potLTIJTN1QVYbL1MrglF3mIq-aHUUylVcwrTWrl
# Okta URL: https://dev-20578441
