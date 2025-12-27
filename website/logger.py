import logging
import os
import time
import datetime
from sense_hat import SenseHat

sense = SenseHat()
LOGFILE = "sensor_log.txt"
delay = 60

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s"
)


def log_readings():
    if not os.path.isfile(LOGFILE):
        with open(LOGFILE, "a") as f:
            f.write("Timestamp\tNorth\tX\tY\tZ\tTemperature\tHumidity\tPressure\n")

    while True:
        try:
            acc = sense.get_accelerometer_raw()
            row = (
                f"{datetime.datetime.now().isoformat()}\t"
                f"{sense.get_compass()}\t"
                f"{acc['x']}\t{acc['y']}\t{acc['z']}\t"
                f"{sense.get_temperature()}\t"
                f"{sense.get_humidity()}\t"
                f"{sense.get_pressure()}\n"
            )
            with open(LOGFILE, "a") as f:
                f.write(row)

        except Exception as e:
            logging.error(e)

        time.sleep(delay)


if __name__ == "__main__":
    logging.info("Starting logger")
