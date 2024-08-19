from workflow.gmail_gdrive import GmailToDriveWorkflow


workflows = {"1":
                 {"metadata": {"name": "gmail_gdrive",
                               "source_app": [{"app_name": "gmail",
                                               "suite": "google",
                                               "actions": ["read"]}],
                               "destination_app": [{"app_name": "google_drive",
                                                    "suite": "google",
                                                    "actions": ["upload"]}]
                               },
                  "steps": GmailToDriveWorkflow
                  }
             }