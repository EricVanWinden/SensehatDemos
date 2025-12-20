import logging.config
from sense_hat import SenseHat
from number_matrix import NumberMatrix


class Accelerometer:
    def __init__(self):
        self.sense = SenseHat()
        self.nm = NumberMatrix()

    def run(self):
        logging.info("Accelerometer, arrow is pointing up. Press Ctrl-C to exit")
        try:
            while True:
                acceleration = self.sense.get_accelerometer_raw()
                x = acceleration['x']
                y = acceleration['y']
                z = acceleration['z']
                maximum = max(abs(x), abs(y), abs(z))
                if maximum > 1:
                    color = self.nm.red
                else:
                    color = self.nm.on

                arrow = self.nm.make_arrow(color)
                pixels = self.nm.create_pixels(arrow)
                self.sense.set_pixels(pixels)
                x = round(x, 0)
                y = round(y, 0)
                z = round(z, 0)

                logging.debug(str(x) + " " + str(y) + " " + str(z) + " " + str(maximum))
                if x == -1:
                    self.sense.set_rotation(180)
                elif y == 1:
                    self.sense.set_rotation(90)
                elif y == -1:
                    self.sense.set_rotation(270)
                else:
                    self.sense.set_rotation(0)

        except KeyboardInterrupt:
            self.sense.set_pixels(self.nm.all_same_2d(self.nm.off))
            logging.info("Accelerometer demo stopped")
