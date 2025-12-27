import os
from flasgger import Swagger
import logging
import time
import requests
import numpy as np
from flask import Flask, Response, request, render_template, send_from_directory
from waitress import serve

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/")
def home():
    """
    Sensehat homepage.
    ---
    tags:
      - UI
    summary: Display the Sensehat control panel
    description: |
      Returns a simple HTML interface with buttons for:
        - **Live Motion Stream** (`/motion`)
        - **Take Snapshot** (`/snapshot`)

      This endpoint serves the user interface rather than a JSON API.
    responses:
      200:
        description: HTML control panel
        content:
          text/html:
            schema:
              type: string
              example: "<html>...</html>"
    """
    return render_template("home.html")


@app.route('/health')
def health():
    """
    Health check endpoint.
    ---
    tags:
      - System
    summary: Check if the service is running
    description: Returns **OK** when the service is alive and responsive.
    responses:
      200:
        description: Service is healthy
        content:
          text/plain:
            schema:
              type: string
              example: OK
    """
    return "OK"


if __name__ == "__main__":
    logging.info("Starting Waitress server on port 8081")
    serve(app, host="0.0.0.0", port=8081)
