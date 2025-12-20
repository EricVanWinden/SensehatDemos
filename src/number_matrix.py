import numpy as np
import math as math


class NumberMatrix:
    def __init__(self):
        self.off = [0, 0, 0]
        self.on = [255, 255, 255]

    def create_matrix(self, number):
        """
        Generates an 8 * 8 matrix that can be displayed self.on the sense hat
        :param number: the number to display
        """
        self.on = [255, 255, 255]
        self.off = [0, 0, 0]
        matrix = np.array([
            [self.off, self.off, self.off, self.off, self.off, self.off, self.off, self.off],
            [self.off, self.off, self.off, self.off, self.off, self.off, self.off, self.off],
            [self.off, self.off, self.off, self.off, self.off, self.off, self.off, self.off],
            [self.off, self.off, self.off, self.off, self.off, self.off, self.off, self.off],
            [self.off, self.off, self.off, self.off, self.off, self.off, self.off, self.off],
            [self.off, self.off, self.off, self.off, self.off, self.off, self.off, self.off],
            [self.off, self.off, self.off, self.off, self.off, self.off, self.off, self.off],
            [self.off, self.off, self.off, self.off, self.off, self.off, self.off, self.off],
        ])

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
        return [
            matrix[0, 0], matrix[1, 0], matrix[2, 0], matrix[3, 0], matrix[4, 0], matrix[5, 0], matrix[6, 0],
            matrix[7, 0],
            matrix[0, 1], matrix[1, 1], matrix[2, 1], matrix[3, 1], matrix[4, 1], matrix[5, 1], matrix[6, 1],
            matrix[7, 1],
            matrix[0, 2], matrix[1, 2], matrix[2, 2], matrix[3, 2], matrix[4, 2], matrix[5, 2], matrix[6, 2],
            matrix[7, 2],
            matrix[0, 3], matrix[1, 3], matrix[2, 3], matrix[3, 3], matrix[4, 3], matrix[5, 3], matrix[6, 3],
            matrix[7, 3],
            matrix[0, 4], matrix[1, 4], matrix[2, 4], matrix[3, 4], matrix[4, 4], matrix[5, 4], matrix[6, 4],
            matrix[7, 4],
            matrix[0, 5], matrix[1, 5], matrix[2, 5], matrix[3, 5], matrix[4, 5], matrix[5, 5], matrix[6, 5],
            matrix[7, 5],
            matrix[0, 6], matrix[1, 6], matrix[2, 6], matrix[3, 6], matrix[4, 6], matrix[5, 6], matrix[6, 6],
            matrix[7, 6],
            matrix[0, 7], matrix[1, 7], matrix[2, 7], matrix[3, 7], matrix[4, 7], matrix[5, 7], matrix[6, 7],
            matrix[7, 7],
        ]

    def all_same(self, same_value):
        return [
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value,
            same_value, same_value, same_value, same_value, same_value, same_value, same_value, same_value]
