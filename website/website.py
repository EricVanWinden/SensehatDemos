import os
from flasgger import Swagger
import logging
import time
import requests
import numpy as np
from flask import Flask, Response, request, render_template, send_from_directory
from waitress import serve
from sense_hat import SenseHat

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)
swagger = Swagger(app)

sense = SenseHat()


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


@app.route('/all_sensors')
def all_sensors():
    """
    Get all Sense HAT sensor readings
    ---
    tags:
      - SenseHat
    summary: Read all sensors from the Sense HAT
    description: Returns compass, accelerometer, temperature, humidity, and pressure values in an HTML table.
    responses:
      200:
        description: HTML table containing all sensor values
        content:
          text/html:
            schema:
              type: string
              example: "<html>...</html>"
    """
    north = sense.get_compass()
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    t = sense.get_temperature()
    rh = sense.get_humidity()
    p = sense.get_pressure()

    html = f"""
    <html>
      <head>
        <title>All Sensors</title>
        <style>
          table {{
            border-collapse: collapse;
          }}
          th, td {{
            border: 1px solid #555;
            padding: 4px 8px;
          }}
          th {{
            background-color: #eee;
          }}
        </style>
      </head>
      <body>
        <h1>All Sensors</h1>
        <table>
          <tr><th>Output</th><th>Value</th></tr>
          <tr><td>Compass (north)</td><td>{north:.2f}</td></tr>
          <tr><td>Accel X</td><td>{x:.4f}</td></tr>
          <tr><td>Accel Y</td><td>{y:.4f}</td></tr>
          <tr><td>Accel Z</td><td>{z:.4f}</td></tr>
          <tr><td>Temperature (°C)</td><td>{t:.2f}</td></tr>
          <tr><td>Humidity (%)</td><td>{rh:.2f}</td></tr>
          <tr><td>Pressure (mbar)</td><td>{p:.2f}</td></tr>
        </table>
      </body>
    </html>
    """
    return html


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
