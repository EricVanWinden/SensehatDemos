from Xyz import *
from IlluminantData import *


class ReflectionCurve:
    """
    class containing a reflection curve
    """

    def __init__(self, curve):
        """
        constructor
        """
        self.illuminant = IlluminantData()
        assert len(curve) == self.illuminant.count
        self.curve = curve

    def get_xyz(self):
        """
        Calculates the XYZ values of this reflection curve
        """

        x_sum = 0.0
        y_sum = 0.0
        z_sum = 0.0
        counter = 0

        for r in self.curve:
            x_sum += r * self.illuminant.x[counter]
            y_sum += r * self.illuminant.y[counter]
            z_sum += r * self.illuminant.z[counter]
            counter += 1

        return Xyz(x_sum, y_sum, z_sum, self.illuminant)
