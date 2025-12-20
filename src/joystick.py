import logging.config
from sense_hat import SenseHat
from number_matrix import NumberMatrix


class Joystick:
    def __init__(self):
        self.sense = SenseHat()
        self.nm = NumberMatrix()

    def run(self):
        logging.info("Use joystick to move the dot. Hold middle to stop")
        matrix = self.nm.all_same_3d(self.nm.off)
        x = 4
        y = 4
        matrix[x, y] = self.nm.on
        pixels = self.nm.create_pixels(matrix)
        self.sense.set_pixels(pixels)

        busy = True
        while busy:
            for event in self.sense.stick.get_events():
                if (event.direction == 'middle') & (event.action == 'held'):
                    busy = False

                if (event.action == 'pressed') | (event.action == 'held'):
                    if event.direction == 'up':
                        if y > 0:
                            matrix[x, y] = self.nm.off
                            y -= 1
                            matrix[x, y] = self.nm.green
                        else:
                            matrix[x, y] = self.nm.red

                    if event.direction == 'down':
                        if y < 7:
                            matrix[x, y] = self.nm.off
                            y += 1
                            matrix[x, y] = self.nm.green
                        else:
                            matrix[x, y] = self.nm.red

                    if event.direction == 'left':
                        if x > 0:
                            matrix[x, y] = self.nm.off
                            x -= 1
                            matrix[x, y] = self.nm.green
                        else:
                            matrix[x, y] = self.nm.red

                    if event.direction == 'right':
                        if x < 7:
                            matrix[x, y] = self.nm.off
                            x += 1
                            matrix[x, y] = self.nm.green
                        else:
                            matrix[x, y] = self.nm.red

                if event.action == 'released':
                    matrix[x, y] = self.nm.on

                pixels = self.nm.create_pixels(matrix)
                self.sense.set_pixels(pixels)

        self.sense.set_pixels(self.nm.all_same_2d(self.nm.off))
        logging.info("Joystick demo stopped")
