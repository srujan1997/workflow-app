from google.oauth2.credentials import Credentials
from utils.json import read_json_file
from workflow.models import applications


class GoogleAuth:
    def __init__(self, user_id=None, workflow_id=None):
        self.creds = None
        self.user_id = user_id
        self.workflow_id = workflow_id

    def __get_scopes__(self):
        scopes = []
        user_data = read_json_file("user/models.json")

        from workflow.workflow_models import workflows

        if self.workflow_id in user_data[self.user_id]["workflows"]:
            metadata = workflows[self.workflow_id]["metadata"]
            source_apps = metadata["source_app"]
            for app in source_apps:
                app_name = app["app_name"]
                if app["suite"] == "google":
                    for action in app["actions"]:
                        scopes.append(applications["google"][app_name][action])

            destination_apps = metadata["destination_app"]
            for app in destination_apps:
                app_name = app["app_name"]
                if app["suite"] == "google":
                    for action in app["actions"]:
                        scopes.append(applications["google"][app_name][action])

            return scopes

    def mock_exchange_code_for_credentials(self, auth_code, scopes=[]):

        if self.user_id and self.workflow_id:
            scopes = self.__get_scopes__()

        mock_creds = Credentials(
            token="mock_access_token",
            refresh_token="mock_refresh_token",
            token_uri="https://oauth2.googleapis.com/token",
            client_id="client-id",
            client_secret="client-secret",
            scopes=scopes
        )

        self.creds = mock_creds
        return mock_creds

    def store_credentials(self, creds):
        with open(f"user/secrets/workflow_{self.workflow_id}/{self.user_id}_token.json", "w") as file:
            file.write(creds.to_json())

    @property
    def get_credentials(self):
        return self.creds
