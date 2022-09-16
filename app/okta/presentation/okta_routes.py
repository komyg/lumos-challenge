from flask import Blueprint

from . import okta_controller as controller

okta_blueprint = Blueprint("okta", __name__, url_prefix="/okta")

okta_blueprint.route("/users", methods=["GET"])(controller.list_users)
