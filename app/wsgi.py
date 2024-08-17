#!/usr/bin/env python3

"""
This module creates a flask instance and ties it up with blueprints
"""
from app import create_app


app = create_app(app_name="WORKFLOW_SERVICE")


if __name__ == "__main__":
    app.run(host=app.config["HOST_IP"], port=app.config["APP_PORT"])
