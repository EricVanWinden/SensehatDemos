from inspect import stack
import logging
import os
import time
import datetime
import sys
import serial
from sense_hat import SenseHat

sense = SenseHat()
LOGFILE = "/home/pi/SensehatDemos/website/sensor_log.txt"
LOGFILE_P1 = "/home/pi/SensehatDemos/website/p1_log.txt"
delay = 60
p1_headers = [
    "Meter type",
    "DSMR version",
    "Time",
    "Electricity meter ID",
    "off-peak day",
    "peak day",
    "off-peak return",
    "peak return",
    "Consumed power",
    "Returned power",
    "Tarief indicator",
    "Power failures",
    "Long failures",
    "Power failure log",
    "Voltage sags L1",
    "Voltage swells L1",
    "Message code",
    "Voltage L1",
    "Current L1",
    "Power L1 consumed",
    "Power L1 returned",
    "Gas meter type",
    "Gas meter ID",
    "Gas",
    "Checksum",
]

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s"
)


def between_parentheses(value):
    start = value.find("(")
    end = value.rfind(")")
    if start == -1 or end == -1 or end <= start:
        return ""
    parsed = value[start + 1:end]
    return parsed.split("*", 1)[0]


def log_readings():
    # Set COM port config
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.stopbits = serial.STOPBITS_ONE
    ser.xonxoff = 0
    ser.rtscts = 0
    ser.timeout = 20
    ser.port = "/dev/ttyUSB0"
    ser_active = False

    if not os.path.isfile(LOGFILE):
        with open(LOGFILE, "a") as f:
            f.write("Timestamp\tNorth\tX\tY\tZ\tTemperature\tHumidity\tPressure\n")

    if not os.path.isfile(LOGFILE_P1):
        with open(LOGFILE_P1, "a") as f:
            f.write("\t".join(p1_headers) + "\n")

    while True:
        time.sleep(delay)
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

        if not ser_active:
            try:
                ser.open()
                ser_active = True
            except:
                ser_active = False

        if ser_active:
            try:
                stack = []
                while True:
                    p1_raw = ser.readline()
                    p1_line = "".join(ch for ch in p1_raw.decode("utf-8", errors="ignore") if ch.isprintable()).strip()
                    stack.append(p1_line)
                    if p1_line.startswith("!"):
                        break

                values = [""] * len(p1_headers)
                for line in stack:
                    if line.startswith("/"):
                        values[0] = line
                    elif line.startswith("1-3:0.2.8"):
                        values[1] = between_parentheses(line)
                    elif line.startswith("0-0:1.0.0"):
                        values[2] = between_parentheses(line)
                    elif line.startswith("0-0:96.1.1"):
                        values[3] = between_parentheses(line)
                    elif line.startswith("1-0:1.8.1"):
                        values[4] = line[10:19]
                    elif line.startswith("1-0:1.8.2"):
                        values[5] = line[10:19]
                    elif line.startswith("1-0:2.8.1"):
                        values[6] = line[10:19]
                    elif line.startswith("1-0:2.8.2"):
                        values[7] = line[10:19]
                    elif line.startswith("1-0:1.7.0"):
                        values[8] = int(float(line[10:16]) * 1000)
                    elif line.startswith("1-0:2.7.0"):
                        values[9] = int(float(line[10:16]) * 1000)
                    elif line.startswith("0-0:96.14.0"):
                        values[10] = between_parentheses(line)
                    elif line.startswith("0-0:96.7.21"):
                        values[11] = between_parentheses(line)
                    elif line.startswith("0-0:96.7.9"):
                        values[12] = between_parentheses(line)
                    elif line.startswith("1-0:99.97.0"):
                        values[13] = line
                    elif line.startswith("1-0:32.32.0"):
                        values[14] = between_parentheses(line)
                    elif line.startswith("1-0:32.36.0"):
                        values[15] = between_parentheses(line)
                    elif line.startswith("0-0:96.13.0"):
                        values[16] = between_parentheses(line)
                    elif line.startswith("1-0:32.7.0"):
                        values[17] = between_parentheses(line)
                    elif line.startswith("1-0:31.7.0"):
                        values[18] = between_parentheses(line)
                    elif line.startswith("1-0:21.7.0"):
                        values[19] = between_parentheses(line)
                    elif line.startswith("1-0:22.7.0"):
                        values[20] = between_parentheses(line)
                    elif line.startswith("0-1:24.1.0"):
                        values[21] = between_parentheses(line)
                    elif line.startswith("0-1:96.1.0"):
                        values[22] = between_parentheses(line)
                    elif line.startswith("0-1:24.2.1"):
                        values[23] = int(float(line[26:35]) * 1000)
                    elif line.startswith("!"):
                        values[24] = line
                    else:
                        logging.debug(f'Unrecognized line: {line}')

                with open(LOGFILE_P1, "a") as f:
                    f.write("\t".join(values) + "\n")
            except Exception as e:
                logging.error(e)


if __name__ == "__main__":
    logging.info("Starting logger")
    log_readings()
