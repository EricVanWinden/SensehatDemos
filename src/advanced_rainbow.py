from time import sleep
import logging.config
from sense_hat import SenseHat
from reflection_curve import *
from illuminant_data import IlluminantData
from curve_creator import *
from number_matrix import *


class AdvancedRainbow:
    def __init__(self):
        self.d65 = IlluminantData()
        self.sense = SenseHat()
        self.nm = NumberMatrix()

    def run(self):
        matrix = self.nm.all_same_3d(self.nm.off)

        # looping over wavelengths
        i = 0
        started = False

        logging.info("generating all colors of the rainbow. Press Ctrl-C to exit")
        try:
            while True:
                index = i
                if (index > 7) | started:
                    started = True
                    index = 7
                    for j in range(7):
                        matrix[j] = matrix[j + 1]

                for j in range(8):
                    # increasing the band width in every row
                    curve = create_curve(self.d65.count, i, j * 3)
                    xyz = ReflectionCurve(curve).get_xyz()
                    rgb = xyz.get_rgb()
                    matrix[index, j, 0] = rgb.r_norm
                    matrix[index, j, 1] = rgb.g_norm
                    matrix[index, j, 2] = rgb.b_norm

                pixels = self.nm.create_pixels(matrix)
                self.sense.set_pixels(pixels)

                sleep(0.1)
                i += 1
                if i >= 60:
                    i = 0

        except KeyboardInterrupt:
            self.sense.set_pixels(self.nm.all_same_2d(self.nm.off))
            logging.info("Advanced rainbow demo stopped")
