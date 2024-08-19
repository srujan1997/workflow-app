from unittest.mock import Mock


class GmailService:

    @classmethod
    def get_mock_gmail_service(cls, credentials):
        # Credentials are necessary for GoogleAPI's
        mock_gmail_service = Mock()

        # Mock Gmail API responses
        mock_gmail_service.users().messages().list.return_value.execute.return_value = {
            'messages': [{'id': '123'}]
        }
        mock_gmail_service.users().messages().get.return_value.execute.return_value = {
            'payload': {
                'parts': [
                    {'filename': 'attachment.txt', 'body': {'attachmentId': 'attachment123'}}
                ]
            }
        }
        mock_gmail_service.users().messages().attachments().get.return_value.execute.return_value = {
            'data': 'hi'
        }

        return mock_gmail_service
