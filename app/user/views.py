from flask import request

from . import user
from http_response import success_response, error_response


@user.route("/google/authorize", methods=["POST"])
def get_integrations():
    auth_code = request.args.get("auth")
    if not auth_code:
        return error_response(400, "Requires authorization code.")


    return success_response(res)