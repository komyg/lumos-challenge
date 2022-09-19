from flask import Blueprint, Flask

from . import capabilities_controller as controller


def get_capabilities_blueprint(app: Flask):
    blueprint = Blueprint("capabilities", __name__, url_prefix="/capabilities")
    blueprint.route("/", methods=["GET"])(controller.create_capabilities_handler(app))
    return blueprint
