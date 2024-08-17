from flask import request
import json


from . import workflow
from workflow.models import integrations
from http_response import success_response, error_response


@workflow.route("/integrations", methods=["GET"])
def get_integrations():
    res = {}
    for integration in integrations:
        if integrations[integration]["status"]: res[integration] = integrations[integration]["description"]

    return success_response(res)


# filename = request.args.get("filename")