from flask import Flask

from config import Config
from ping import ping


def create_app(app_name=""):
    """
    Description: Flask app factory method with all app contexts.
    :param app_name: string
    :return: app (Flask app)
    """
    app = Flask(app_name)

    app_config = Config
    app.config.from_object(app_config)

    app.url_map.strict_slashes = False

    BASE_URL_PREFIX = f"/api"

    with app.app_context():
        app.register_blueprint(ping, url_prefix=f"{BASE_URL_PREFIX}/ping")

    @app.teardown_request
    def teardown_request(exception):
        #  To snapshot service state and gracefully close the application. Currently, doing nothing.
        pass

    return app
