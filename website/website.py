import logging
import requests
import datetime
from collections import deque
from flasgger import Swagger
from flask import Flask, Response, request, render_template, send_from_directory
from sense_hat import SenseHat
from waitress import serve
from number_matrix import NumberMatrix

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)
swagger = Swagger(app)

sense = SenseHat()
rotation = 0
sense.set_rotation(rotation)
last_readings = None
units = {
    "North": "Degrees",
    "X": "-",
    "Y": "-",
    "Z": "-",
    "Temperature": "°C",
    "Humidity": "%",
    "Pressure": "mbar"
}
LOG_DIR = "/home/pi/SensehatDemos/website"
LOGFILE = "sensor_log.txt"


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


@app.route("/graph")
def graph():
    """
    Sensehat graph page.
    ---
    tags:
      - SenseHat
    responses:
      200:
        description: HTML graph
    """
    return render_template("graph.html")


@app.route("/download_log")
def download_log():
    """
    Download the sensor log file.

    ---
    tags:
      - SenseHat
    get:
      description: Download the tab‑delimited Sense HAT sensor log.
      responses:
        200:
          description: The sensor_log.txt file will be downloaded.
          content:
            text/plain:
              schema:
                type: string
                format: binary
    """
    return send_from_directory(
        LOG_DIR,
        LOGFILE,
        as_attachment=True
    )


@app.route("/sensor_data")
def sensor_data():
    """
    Return logged sensor data as JSON.
    ---
    get:
      description: Returns parsed sensor_log.txt as JSON for graphing.
      responses:
        200:
          description: JSON array of sensor readings.
    """
    max_lines = 60 * 24
    with open(f"{LOG_DIR}/{LOGFILE}") as f:
        lines = deque(f, max_lines + 1)

    data = []
    for line in list(lines)[1:]:
        parts = line.strip().split("\t")
        ts = datetime.datetime.fromisoformat(parts[0])
        data.append({
            "timestamp": parts[0],
            "time_hm": ts.strftime("%H:%M"),
            "temperature": float(parts[5]),
            "humidity": float(parts[6]),
            "pressure": float(parts[7])
        })

    return data


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
    acceleration = sense.get_accelerometer_raw()
    readings = {
        "North": sense.get_compass(),
        "X": acceleration['x'],
        "Y": acceleration['y'],
        "Z": acceleration['z'],
        "Temperature": sense.get_temperature(),
        "Humidity": sense.get_humidity(),
        "Pressure": sense.get_pressure()
    }
    global last_readings
    if last_readings is None:
        last_readings = readings

    html = """
    <html>
  <head>
    <title>All Sensors</title>
    <style>
      table {
        border-collapse: collapse;
        width: auto;
      }
      table tr:first-child th {
        border-top: 2px solid #555;
      }
      th {
        background-color: #eee;
        border-bottom: 2px solid #555;
        padding: 4px 8px;
        text-align: center;
      }
      td, th {
        border-left: 1px solid #555;
        border-right: 1px solid #555;
        padding: 4px 8px;
      }
      td:first-child {
        text-align: left;
      }
      td:not(:first-child) {
        text-align: center;
      }
      table tr:last-child td {
        border-bottom: 2px solid #555;
      }
    </style>
  </head>
      <body>
        <h1>All Sensors</h1>
        <table>
          <tr><th>Output</th><th>Value</th><th>Last</th><th>Unit</th></tr>
    """
    for reading in readings:
        if reading in ("X", "Y", "Z"):
            value = f"{readings[reading]:.3f}"
            last_value = f"{last_readings[reading]:.3f}"
        else:
            value = f"{readings[reading]:.0f}"
            last_value = f"{last_readings[reading]:.0f}"

        html += f"<tr><td>{reading}</td><td>{value}</td><td>{last_value}</td><td>{units[reading]}</td></tr>"

    last_readings = readings
    html += """
            </table>
          </body>
        </html>
        """
    return html


@app.route('/rotate_matrix')
def rotate_matrix():
    """
    Rotates the SenseHat matrix by 90 degrees and returns the new value.
    ---
    tags:
      - SenseHat
    summary: rotates the SenseHat matrix
    description: rotates the SenseHat matrix.
    responses:
      200:
        description: the new rotation value
    """
    global rotation
    rotation += 90
    if rotation == 360:
        rotation = 0
    sense.set_rotation(rotation)
    return {"rotation": rotation}


@app.route('/use_joystick')
def use_joystick():
    """
    Use the joystick to move the dot on the LED screen
    ---
    tags:
      - SenseHat
    summary: rotates the SenseHat matrix
    description: rotates the SenseHat matrix.
    responses:
      200:
        description: the new rotation value
    """
    logging.info("Use joystick to move the dot. Hold middle to stop")
    nm = NumberMatrix()
    matrix = nm.all_same_3d(nm.off)
    x = 4
    y = 4
    matrix[x, y] = nm.on
    pixels = nm.create_pixels(matrix)
    sense.set_pixels(pixels)

    busy = True
    while busy:
        for event in sense.stick.get_events():
            if (event.direction == 'middle') & (event.action == 'held'):
                busy = False

            if (event.action == 'pressed') | (event.action == 'held'):
                if event.direction == 'up':
                    if y > 0:
                        matrix[x, y] = nm.off
                        y -= 1
                        matrix[x, y] = nm.green
                    else:
                        matrix[x, y] = nm.red

                if event.direction == 'down':
                    if y < 7:
                        matrix[x, y] = nm.off
                        y += 1
                        matrix[x, y] = nm.green
                    else:
                        matrix[x, y] = nm.red

                if event.direction == 'left':
                    if x > 0:
                        matrix[x, y] = nm.off
                        x -= 1
                        matrix[x, y] = nm.green
                    else:
                        matrix[x, y] = nm.red

                if event.direction == 'right':
                    if x < 7:
                        matrix[x, y] = nm.off
                        x += 1
                        matrix[x, y] = nm.green
                    else:
                        matrix[x, y] = nm.red

            if event.action == 'released':
                matrix[x, y] = nm.on

            pixels = nm.create_pixels(matrix)
            sense.set_pixels(pixels)

    sense.set_pixels(nm.all_same_2d(nm.off))
    msg = "Joystick demo stopped"
    logging.info(msg)
    return msg


@app.route("/display_text", methods=["POST"])
def display_text():
    """
    Displays the text on the SenseHat matrix.
    ---
    tags:
      -  SenseHat
    requestBody:
      required: true
    responses:
      200:
        description: text is displayed
      400:
        description: Invalid or missing text
      500:
        description: Processing error
    """
    text_to_display = request.form.get("text_to_display", "").strip()
    repeats = int(request.form.get('repeats', "5"))
    if not text_to_display:
        return "Text required", 400

    for i in range(repeats):
        sense.show_message(text_to_display)
    return f"Displayed {text_to_display}"


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
