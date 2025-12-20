import string
from time import sleep
import logging.config
from sense_hat import SenseHat
from number_matrix import NumberMatrix


class Alphabet:
    def __init__(self):
        self.sense = SenseHat()
        self.nm = NumberMatrix()

    def run(self):
        logging.info("Show the alpabet")
        try:
            for c in string.ascii_uppercase:
                self.sense.show_letter(c)
                sleep(0.5)

            self.sense.set_pixels(self.nm.all_same_2d(self.nm.off))
            logging.info("Alphabet stopped")

        except KeyboardInterrupt:
            self.sense.set_pixels(self.nm.all_same_2d(self.nm.off))
            logging.info("Alphabet stopped")
