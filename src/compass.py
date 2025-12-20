from time import sleep
import logging.config
from sense_hat import SenseHat
from number_matrix import NumberMatrix

class Compass:
    def __init__(self):
        self.sense = SenseHat()
        self.nm = NumberMatrix()

    def run(self):
        logging.info("Compass, dot is pointing north. Press Ctrl-C to exit")
        self.sense.set_pixels(self.nm.all_same_2d(self.nm.off))
        try:
            while True:
                north = self.sense.get_compass()
                coordinate = calculate_coordinate(north)
                for j in range(coordinate.__len__()):
                    self.sense.set_pixel(coordinate[j][0], coordinate[j][1], self.nm.on)
                sleep(0.1)
                for j in range(coordinate.__len__()):
                    self.sense.set_pixel(coordinate[j][0], coordinate[j][1], self.nm.off)
        except KeyboardInterrupt:
            self.sense.set_pixels(self.nm.all_same_2d(self.nm.off))
            logging.info("Compass stopped")

def calculate_coordinate(degrees):
    x = int(math.cos(degrees * math.pi / 180) * 4.0) + 4
    y = int(math.sin(degrees * math.pi / 180) * -4.0) + 4
    if x == 8:
        return [[7, 3], [7, 4]]
    if x == 0:
        return [[0, 3], [0, 4]]
    if y == 8:
        return [[3, 7], [4, 7]]
    if y == 0:
        return [[3, 0], [4, 0]]

    if y < 4:
        y -= 1

    if x < 4:
        x -= 1

    return [[x, y]]
