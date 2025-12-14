class Rgb:
    """
    Class to store RGB data
    """

    def __init__(self, r, g, b, illuminant_data):
        """
        constructor
        """
        self.r = r
        self.g = g
        self.b = b
        self.illuminant_data = illuminant_data
        maximum = max(self.r, self.g, self.b)

        self.r_norm = self.r * 255.0 / maximum
        if self.r_norm < 0:
            self.r_norm = 0

        self.g_norm = self.g * 255.0 / maximum
        if self.g_norm < 0:
            self.g_norm = 0

        self.b_norm = self.b * 255.0 / maximum
        if self.b_norm < 0:
            self.b_norm = 0
