workflows = dict(id=1, name="gmail_gdrive", steps="<workflow_obj>")


applications = {"google":
                    {"gmail": {"read": "https://www.googleapis.com/auth/gmail.readonly"},
                     "google_drive": {"upload": "https://www.googleapis.com/auth/drive.file"},
                     },
                }

integrations = {
    "gmail_gdrive": {"source_app": "gmail",
                     "destination_app": "google_drive",
                     "description": "Upload attachments in mails to google drive",
                     "status": 1}
}
