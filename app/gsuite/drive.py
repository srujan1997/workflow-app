from unittest.mock import Mock


class DriveService:

    @classmethod
    def get_mock_drive_service(cls, credentials):
        # Credentials are necessary for GoogleAPI's
        mock_drive_service = Mock()

        # Mock Drive API response
        mock_drive_service.files().create.return_value.execute.return_value = {
            'id': 'drive_file_id_1'
        }

        return mock_drive_service
