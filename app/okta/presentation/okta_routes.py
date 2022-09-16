from flask import Blueprint

from . import okta_controller as controller

okta_blueprint = Blueprint("okta", __name__, url_prefix="/okta")

okta_blueprint.route("/users", methods=["GET"])(controller.list_users)
okta_blueprint.route("/users/<user_id>/suspend", methods=["POST"])(
    controller.suspend_user
)
okta_blueprint.route("/users/<user_id>/unsuspend", methods=["POST"])(
    controller.unsuspend_user
)
okta_blueprint.route("/users/<user_id>", methods=["DELETE"])(controller.delete_user)
