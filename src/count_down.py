from time import sleep
import logging.config
from sense_hat import SenseHat
from number_matrix import NumberMatrix


class CountDown:
    def __init__(self):
        self.sense = SenseHat()
        self.nm = NumberMatrix()

    def run(self):
        logging.info("Counting down from 99 to 0 on LED matrix")
        try:
            for i in range(101):
                matrix = self.nm.create_matrix(99 - i)
                pixels = self.nm.create_pixels(matrix)
                self.sense.set_pixels(pixels)
                sleep(0.3)
        except KeyboardInterrupt:
            self.sense.set_pixels(self.nm.all_same_2d(self.nm.off))
            logging.info("Compass stopped")
