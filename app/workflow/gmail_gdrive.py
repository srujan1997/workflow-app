from gsuite.auth import GoogleAuth
from gsuite.gmail import GmailService
from gsuite.drive import DriveService


class GmailToDriveWorkflow(GoogleAuth):
    def __init__(self, user_id, workflow_id, folder_id=None):
        super().__init__(user_id, workflow_id)
        self.creds = GoogleAuth.get_credentials
        self.gmail_service = GmailService.get_mock_gmail_service(self.creds)
        self.drive_service = DriveService.get_mock_drive_service(self.creds)
        self.folder_id = folder_id

    def run(self):
        messages = self.gmail_service.users().messages().list(userId="me", q="has:attachment is:unread").execute().get(
            'messages', [])
        uploaded_files = []

        for message in messages:
            msg = self.gmail_service.users().messages().get(userId="me", id=message['id']).execute()
            for part in msg['payload']['parts']:
                if part['filename']:
                    attachment = self.gmail_service.users().messages().attachments().get(
                        userId="me", messageId=message["id"], id=part["body"]["attachmentId"]
                    ).execute()
                    uploaded_file = self.drive_service.files().create(body={'name': part['filename']}).execute()
                    uploaded_files.append(uploaded_file)

        return uploaded_files
