from time import sleep
import logging.config
from sense_hat import SenseHat
from number_matrix import NumberMatrix


class Weather:
    def __init__(self):
        self.sense = SenseHat()
        self.nm = NumberMatrix()

    def run(self):
        logging.info("Weather is shown on LED matrix. Press Ctrl-C to exit")
        try:
            while True:
                t = int(self.sense.get_temperature())
                self.sense.show_letter("T")
                sleep(0.5)
                matrix = self.nm.create_matrix(t)
                pixels = self.nm.create_pixels(matrix)
                self.sense.set_pixels(pixels)
                sleep(0.5)
        
                rh = int(self.sense.get_humidity())
                self.sense.show_letter("H")
                sleep(0.5)
                matrix = self.nm.create_matrix(rh)
                pixels = self.nm.create_pixels(matrix)
                self.sense.set_pixels(pixels)
                sleep(0.5)
                
                p = int(self.sense.get_pressure())
                self.sense.show_message("p=" + str(p))
        
        except KeyboardInterrupt:
            self.sense.set_pixels(self.nm.all_same_2d(self.nm.off))
            logging.info("Weather demo stopped")