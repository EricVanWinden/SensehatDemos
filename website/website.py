import os

os.environ["SDL_AUDIODRIVER"] = "alsa"

from flasgger import Swagger
import logging
import time
import cv2
import requests
import numpy as np
from flask import Flask, Response, request, render_template, send_from_directory
from waitress import serve
import pygame

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)
swagger = Swagger(app)

time.sleep(2)
alert = None


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


def ensure_mixer():
    global alert
    if alert is None:
        pygame.mixer.init(buffer=4096)  # larger buffer prevents underruns
        base_dir = os.path.dirname(os.path.abspath(__file__))
        sound_path = os.path.join(base_dir, "mixkit-retro-game-emergency-alarm-1000.wav")
        alert = pygame.mixer.Sound(sound_path)
        logging.info(f"Loaded sound into memory: {sound_path}")


@app.route('/sound')
def sound():
    """
    plays sound on the raspberry pi hosting this website.
    ---
    tags:
      - Sound
    responses:
      200:
        description: sound was played
      500:
        description: sound error
    """
    try:
        ensure_mixer()
        logging.info("Playing alert sound")
        alert.play()
        return "OK"
    except Exception as e:
        logging.exception(f"Error in playing sound: {e}")
        return "Error", 500


if __name__ == "__main__":
    logging.info("Starting Waitress server on port 8081")
    serve(app, host="0.0.0.0", port=8081)
