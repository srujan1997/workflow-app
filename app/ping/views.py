from . import ping
from http_response import success_response


@ping.route("/", methods=["GET"])
def ping_service():
    # Ping API to check health
    return success_response({"data": "pong"})