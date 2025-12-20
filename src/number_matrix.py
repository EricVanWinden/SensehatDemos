import numpy as np
import math as math


class NumberMatrix:
    def __init__(self):
        self.off = [0, 0, 0]
        self.on = [255, 255, 255]
        self.direction = 'V'

    def create_matrix(self, number):
        """
        Generates an 8 * 8 matrix that can be displayed self.on the sense hat
        :param number: the number to display
        """
        matrix = self.all_same_3d(self.off)

        if number < 0:
            return matrix

        elif number < 10:
            sub_matrix = self.create_number(number)
            for x in range(3):
                for y in range(5):
                    matrix[x + 5, y] = sub_matrix[y, x]

            return matrix

        elif number < 100:
            first = math.floor(number / 10)
            sub_matrix = self.create_number(first)
            for x in range(3):
                for y in range(5):
                    matrix[x + 1, y] = sub_matrix[y, x]

            second = number - (first * 10)
            sub_matrix = self.create_number(second)
            for x in range(3):
                for y in range(5):
                    matrix[x + 5, y] = sub_matrix[y, x]

            return matrix
        else:
            return matrix

    def create_number(self, number):
        matrix = np.array([
            [self.off, self.off, self.off],
            [self.off, self.off, self.off],
            [self.off, self.off, self.off],
            [self.off, self.off, self.off],
            [self.off, self.off, self.off],
        ])

        if number == 0:
            matrix[0, 0] = self.on
            matrix[0, 1] = self.on
            matrix[0, 2] = self.on
            matrix[1, 0] = self.on
            matrix[1, 2] = self.on
            matrix[2, 0] = self.on
            matrix[2, 2] = self.on
            matrix[3, 0] = self.on
            matrix[3, 2] = self.on
            matrix[4, 0] = self.on
            matrix[4, 1] = self.on
            matrix[4, 2] = self.on
            return matrix

        if number == 1:
            matrix[0, 2] = self.on
            matrix[1, 2] = self.on
            matrix[2, 2] = self.on
            matrix[3, 2] = self.on
            matrix[4, 2] = self.on
            return matrix

        if number == 2:
            matrix[0, 0] = self.on
            matrix[0, 1] = self.on
            matrix[0, 2] = self.on
            matrix[1, 2] = self.on
            matrix[2, 0] = self.on
            matrix[2, 1] = self.on
            matrix[2, 2] = self.on
            matrix[3, 0] = self.on
            matrix[4, 0] = self.on
            matrix[4, 1] = self.on
            matrix[4, 2] = self.on
            return matrix

        if number == 3:
            matrix[0, 0] = self.on
            matrix[0, 1] = self.on
            matrix[0, 2] = self.on
            matrix[1, 2] = self.on
            matrix[2, 0] = self.on
            matrix[2, 1] = self.on
            matrix[2, 2] = self.on
            matrix[3, 2] = self.on
            matrix[4, 0] = self.on
            matrix[4, 1] = self.on
            matrix[4, 2] = self.on
            return matrix

        if number == 4:
            matrix[0, 0] = self.on
            matrix[0, 2] = self.on
            matrix[1, 0] = self.on
            matrix[1, 2] = self.on
            matrix[2, 0] = self.on
            matrix[2, 1] = self.on
            matrix[2, 2] = self.on
            matrix[3, 2] = self.on
            matrix[4, 2] = self.on
            return matrix

        if number == 5:
            matrix[0, 0] = self.on
            matrix[0, 1] = self.on
            matrix[0, 2] = self.on
            matrix[1, 0] = self.on
            matrix[2, 0] = self.on
            matrix[2, 1] = self.on
            matrix[2, 2] = self.on
            matrix[3, 2] = self.on
            matrix[4, 0] = self.on
            matrix[4, 1] = self.on
            matrix[4, 2] = self.on
            return matrix

        if number == 6:
            matrix[0, 0] = self.on
            matrix[0, 1] = self.on
            matrix[0, 2] = self.on
            matrix[1, 0] = self.on
            matrix[2, 0] = self.on
            matrix[2, 1] = self.on
            matrix[2, 2] = self.on
            matrix[3, 0] = self.on
            matrix[3, 2] = self.on
            matrix[4, 0] = self.on
            matrix[4, 1] = self.on
            matrix[4, 2] = self.on
            return matrix

        if number == 7:
            matrix[0, 0] = self.on
            matrix[0, 1] = self.on
            matrix[0, 2] = self.on
            matrix[1, 2] = self.on
            matrix[2, 2] = self.on
            matrix[3, 2] = self.on
            matrix[4, 2] = self.on
            return matrix

        if number == 8:
            matrix[0, 0] = self.on
            matrix[0, 1] = self.on
            matrix[0, 2] = self.on
            matrix[1, 0] = self.on
            matrix[1, 2] = self.on
            matrix[2, 0] = self.on
            matrix[2, 1] = self.on
            matrix[2, 2] = self.on
            matrix[3, 0] = self.on
            matrix[3, 2] = self.on
            matrix[4, 0] = self.on
            matrix[4, 1] = self.on
            matrix[4, 2] = self.on
            return matrix

        if number == 9:
            matrix[0, 0] = self.on
            matrix[0, 1] = self.on
            matrix[0, 2] = self.on
            matrix[1, 0] = self.on
            matrix[1, 2] = self.on
            matrix[2, 0] = self.on
            matrix[2, 1] = self.on
            matrix[2, 2] = self.on
            matrix[3, 2] = self.on
            matrix[4, 0] = self.on
            matrix[4, 1] = self.on
            matrix[4, 2] = self.on
            return matrix

        return matrix

    def print_matrix(self, matrix):
        for y in range(8):
            print(str(matrix[0, y, 0]) + " " +
                  str(matrix[1, y, 0]) + " " +
                  str(matrix[2, y, 0]) + " " +
                  str(matrix[3, y, 0]) + " " +
                  str(matrix[4, y, 0]) + " " +
                  str(matrix[5, y, 0]) + " " +
                  str(matrix[6, y, 0]) + " " +
                  str(matrix[7, y, 0]))

        print()

    def create_pixels(self, matrix):
        values = []
        for i in range(8):
            for j in range(8):
                if self.direction == 'H':
                    values.append(matrix[j, i])
                else:
                    values.append(matrix[i, j])
        return values

    def all_same_2d(self, same_value):
        return [
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value]

    def all_same_3d(self, same_value):
        return np.array([
            [same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value],
            [same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value],
            [same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value],
            [same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value],
            [same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value],
            [same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value],
            [same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value],
            [same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value]])

    def make_gradient_3d(self):
        values = []
        g = 0
        for i in range(8):
            values_i = []
            r = int(i * 32)
            for j in range(8):
                b = int(j * 32)
                values_i.append([r, g, b])
            values.append(values_i)
        return np.array(values)
