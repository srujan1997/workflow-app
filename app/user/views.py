from flask import request

from . import user
from http_response import success_response, error_response
from gsuite.auth import GoogleAuth
from utils.json import read_json_file, write_to_json_file
from workflow.workflow_models import workflows


@user.route("/workflow/add", methods=["POST"])
def add_workflow():
    user_id = request.args.get("user_id")  # This can be changed when authentication layer is developed.
    workflow_id = request.args.get("workflow")
    if not user_id:
        return error_response(400, "Requires a valid user.")

    if not workflow_id:
        return error_response(400, "Select a workflow to add.")

    user_data = read_json_file("user/models.json")
    if user_id not in user_data:
        user_data[user_id] = dict(workflows=[])
    user_data[user_id]["workflows"].append(workflow_id)
    write_to_json_file("user/models.json", user_data)

    return success_response("Workflow Added.")


@user.route("/google/authorize", methods=["POST"])
def get_integrations():
    auth_code = request.args.get("code")
    user_id = request.args.get("user_id", "user1")  # This can be changed when authentication layer is developed.
    workflow_id = request.args.get("workflow_id")
    if not auth_code:
        return error_response(400, "Requires authorization code.")

    if not workflow_id:
        return error_response(400, "Select workflow for this authorization.")

    try:
        auth = GoogleAuth(user_id, workflow_id)
        creds = auth.mock_exchange_code_for_credentials(auth_code)
        auth.store_credentials(creds)
    except Exception as e:
        return error_response(e)

    return success_response("authenticated")


@user.route("/workflow/execute", methods=["POST"])
def execute_workflow():
    user_id = request.args.get("user_id", "1")  # This can be changed when authentication layer is developed.
    workflow_id = request.args.get("workflow_id")
    if not workflow_id:
        return error_response(400, "Select a workflow to execute.")

    try:
        workflow = workflows[workflow_id]["steps"]
        service = workflow(user_id, workflow_id)
        res = service.run()
    except Exception as e:
        return error_response(e)

    return success_response(res)
