from sense_hat import SenseHat
from number_matrix import NumberMatrix


class SandBox:
    def __init__(self):
        self.sense = SenseHat()
        self.nm = NumberMatrix()

    def run(self):
        matrix = self.nm.make_gradient_3d()
        pixels = self.nm.create_pixels(matrix)
        self.sense.set_pixels(pixels)
