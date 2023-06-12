from flask import Blueprint

ENDPOINT_NAME = "/user"

example_blueprint = Blueprint(
    'example_blueprint', __name__, url_prefix=ENDPOINT_NAME)


@example_blueprint.route("/")
def get_all_users():
    return {1: "Vytautas", 2: "Jonas"}


@example_blueprint.route("/greet_user/<user>")
def index(user: str):
    return {"greet": f"Hello {user}"}
