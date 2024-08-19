applications = {"google":
                    {"gmail": {"read": "https://www.googleapis.com/auth/gmail.readonly"},
                     "google_drive": {"upload": "https://www.googleapis.com/auth/drive.file"},
                     },
                }

integrations = {
    "gmail_gdrive": {"source_app": [{"app_name": "gmail", "suite": "google"}],
                     "destination_app": [{"app_name": "google_drive", "suite": "google"}],
                     "description": "Upload attachments in mails to google drive",
                     "status": 1}
}

