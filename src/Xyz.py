from Lab import *
from Rgb import *


class Xyz:
    """
    Class to store XYZ
    RGB matrix from http://www.brucelindbloom.com/
    """

    def __init__(self, x, y, z, illuminant_data):
        """
        constructor
        """
        self.x = x
        self.y = y
        self.z = z
        self.illuminant_data = illuminant_data

    def get_lab(self):
        x1 = self.x / self.illuminant_data.x_norm
        x2 = self.y / self.illuminant_data.y_norm
        x3 = self.z / self.illuminant_data.z_norm
        power = 1.0 / 3.0
        num1 = 0.0
        num2 = 0.0
        num3 = 0.0
        if x1 <= 0.00885645167903563:
            num1 = 841.0 / 108.0 * x1 + 4.0 / 29.0
        else:
            num1 = x1 ** power

        if x2 <= 0.00885645167903563:
            num2 = 841.0 / 108.0 * x2 + 4.0 / 29.0
        else:
            num2 = x2 ** power

        if x3 <= 0.00885645167903563:
            num3 = 841.0 / 108.0 * x3 + 4.0 / 29.0
        else:
            num3 = x3 ** power

        return Lab(116.0 * num2 - 16.0, 500.0 * (num1 - num2), 200.0 * (num2 - num3), self.illuminant_data)

    def get_rgb(self):
        x1 = (3.1338561 * self.x - 1.6168667 * self.y - 0.4906146 * self.z) / 100.0
        x2 = (-0.9787684 * self.x + 1.9161415 * self.y + 0.0334540 * self.z) / 100.0
        x3 = (0.0719453 * self.x - 0.2289914 * self.y + 1.4052427 * self.z) / 100.0
        r = 0
        g = 0
        b = 0

        if x1 <= 0.00313066844250063:
            r = 12.92 * x1
        else:
            r = 1.055 * x1 ** (5.0 / 12.0) - 0.055

        if x2 <= 0.00313066844250063:
            g = 12.92 * x2
        else:
            g = 1.055 * x2 ** (5.0 / 12.0) - 0.055

        if x3 <= 0.00313066844250063:
            b = 12.92 * x3
        else:
            b = 1.055 * x3 ** (5.0 / 12.0) - 0.055

        return Rgb(r * 255.0, g * 255.0, b * 255.0, self.illuminant_data)
