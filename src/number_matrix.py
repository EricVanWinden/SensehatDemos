import numpy as np
import math as math


def create_matrix(number):
    """
    Generates an 8 * 8 matrix that can be displayed on the sense hat
    :param number: the number to display
    """
    on = [255, 255, 255]
    off = [0, 0, 0]
    matrix = np.array([
        [off, off, off, off, off, off, off, off],
        [off, off, off, off, off, off, off, off],
        [off, off, off, off, off, off, off, off],
        [off, off, off, off, off, off, off, off],
        [off, off, off, off, off, off, off, off],
        [off, off, off, off, off, off, off, off],
        [off, off, off, off, off, off, off, off],
        [off, off, off, off, off, off, off, off],
    ])

    if number < 0:
        return matrix

    if number < 10:
        sub_matrix = create_number(number, on, off)
        for x in range(3):
            for y in range(5):
                matrix[x + 5, y] = sub_matrix[y, x]

        return matrix

    if number < 100:
        first = math.floor(number / 10)
        sub_matrix = create_number(first, on, off)
        for x in range(3):
            for y in range(5):
                matrix[x + 1, y] = sub_matrix[y, x]

        second = number - (first * 10)
        sub_matrix = create_number(second, on, off)
        for x in range(3):
            for y in range(5):
                matrix[x + 5, y] = sub_matrix[y, x]

        return matrix


def create_number(number, on, off):
    matrix = np.array([
        [off, off, off],
        [off, off, off],
        [off, off, off],
        [off, off, off],
        [off, off, off],
    ])

    if number == 0:
        matrix[0, 0] = on
        matrix[0, 1] = on
        matrix[0, 2] = on
        matrix[1, 0] = on
        matrix[1, 2] = on
        matrix[2, 0] = on
        matrix[2, 2] = on
        matrix[3, 0] = on
        matrix[3, 2] = on
        matrix[4, 0] = on
        matrix[4, 1] = on
        matrix[4, 2] = on
        return matrix

    if number == 1:
        matrix[0, 2] = on
        matrix[1, 2] = on
        matrix[2, 2] = on
        matrix[3, 2] = on
        matrix[4, 2] = on
        return matrix

    if number == 2:
        matrix[0, 0] = on
        matrix[0, 1] = on
        matrix[0, 2] = on
        matrix[1, 2] = on
        matrix[2, 0] = on
        matrix[2, 1] = on
        matrix[2, 2] = on
        matrix[3, 0] = on
        matrix[4, 0] = on
        matrix[4, 1] = on
        matrix[4, 2] = on
        return matrix

    if number == 3:
        matrix[0, 0] = on
        matrix[0, 1] = on
        matrix[0, 2] = on
        matrix[1, 2] = on
        matrix[2, 0] = on
        matrix[2, 1] = on
        matrix[2, 2] = on
        matrix[3, 2] = on
        matrix[4, 0] = on
        matrix[4, 1] = on
        matrix[4, 2] = on
        return matrix

    if number == 4:
        matrix[0, 0] = on
        matrix[0, 2] = on
        matrix[1, 0] = on
        matrix[1, 2] = on
        matrix[2, 0] = on
        matrix[2, 1] = on
        matrix[2, 2] = on
        matrix[3, 2] = on
        matrix[4, 2] = on
        return matrix

    if number == 5:
        matrix[0, 0] = on
        matrix[0, 1] = on
        matrix[0, 2] = on
        matrix[1, 0] = on
        matrix[2, 0] = on
        matrix[2, 1] = on
        matrix[2, 2] = on
        matrix[3, 2] = on
        matrix[4, 0] = on
        matrix[4, 1] = on
        matrix[4, 2] = on
        return matrix

    if number == 6:
        matrix[0, 0] = on
        matrix[0, 1] = on
        matrix[0, 2] = on
        matrix[1, 0] = on
        matrix[2, 0] = on
        matrix[2, 1] = on
        matrix[2, 2] = on
        matrix[3, 0] = on
        matrix[3, 2] = on
        matrix[4, 0] = on
        matrix[4, 1] = on
        matrix[4, 2] = on
        return matrix

    if number == 7:
        matrix[0, 0] = on
        matrix[0, 1] = on
        matrix[0, 2] = on
        matrix[1, 2] = on
        matrix[2, 2] = on
        matrix[3, 2] = on
        matrix[4, 2] = on
        return matrix

    if number == 8:
        matrix[0, 0] = on
        matrix[0, 1] = on
        matrix[0, 2] = on
        matrix[1, 0] = on
        matrix[1, 2] = on
        matrix[2, 0] = on
        matrix[2, 1] = on
        matrix[2, 2] = on
        matrix[3, 0] = on
        matrix[3, 2] = on
        matrix[4, 0] = on
        matrix[4, 1] = on
        matrix[4, 2] = on
        return matrix

    if number == 9:
        matrix[0, 0] = on
        matrix[0, 1] = on
        matrix[0, 2] = on
        matrix[1, 0] = on
        matrix[1, 2] = on
        matrix[2, 0] = on
        matrix[2, 1] = on
        matrix[2, 2] = on
        matrix[3, 2] = on
        matrix[4, 0] = on
        matrix[4, 1] = on
        matrix[4, 2] = on
        return matrix

    return matrix


def print_matrix(matrix):
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


def create_pixels(matrix):
    return [
        matrix[0, 0], matrix[1, 0], matrix[2, 0], matrix[3, 0], matrix[4, 0], matrix[5, 0], matrix[6, 0], matrix[7, 0],
        matrix[0, 1], matrix[1, 1], matrix[2, 1], matrix[3, 1], matrix[4, 1], matrix[5, 1], matrix[6, 1], matrix[7, 1],
        matrix[0, 2], matrix[1, 2], matrix[2, 2], matrix[3, 2], matrix[4, 2], matrix[5, 2], matrix[6, 2], matrix[7, 2],
        matrix[0, 3], matrix[1, 3], matrix[2, 3], matrix[3, 3], matrix[4, 3], matrix[5, 3], matrix[6, 3], matrix[7, 3],
        matrix[0, 4], matrix[1, 4], matrix[2, 4], matrix[3, 4], matrix[4, 4], matrix[5, 4], matrix[6, 4], matrix[7, 4],
        matrix[0, 5], matrix[1, 5], matrix[2, 5], matrix[3, 5], matrix[4, 5], matrix[5, 5], matrix[6, 5], matrix[7, 5],
        matrix[0, 6], matrix[1, 6], matrix[2, 6], matrix[3, 6], matrix[4, 6], matrix[5, 6], matrix[6, 6], matrix[7, 6],
        matrix[0, 7], matrix[1, 7], matrix[2, 7], matrix[3, 7], matrix[4, 7], matrix[5, 7], matrix[6, 7], matrix[7, 7],
    ]
