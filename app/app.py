from enum import Enum

from flask import Flask, request
import requests

app = Flask(__name__)

# API Token: 00potLTIJTN1QVYbL1MrglF3mIq-aHUUylVcwrTWrl
# Okta URL: https://dev-20578441


@app.route("/capabilities/<app_name>", methods=["GET"])
def capabilities(app_name: str):
    """Returns the capabilities of a given integration app"""
    print(app_name)

    # TODO: return a list of capabilities that a given app can do.
    # Capabilities can be strings, ids, whatever makes sense to you
    return "Not implemented!"


@app.route("/<app_name>/<capability_name>", methods=["GET"])
def read(app_name: str, capability_name: str):
    """Runs a read action based on the specified capability and app name"""
    print(app_name, capability_name)

    # TODO: validate the request and then do the operation on the given integration
    return f"Some result from the {capability_name} operation on app {app_name}"


@app.route("/<app_name>/<capability_name>", methods=["POST"])
def mutate(app_name: str, capability_name: str):
    """Runs a mutation action based on the specified capability and app name"""
    req_json = request.get_json()
    print(app_name, capability_name, req_json)

    # TODO: validate the request body and then do the operation on the given integration
    return f"Some result from the mutation operation {capability_name} on app {app_name} - did it work?"
