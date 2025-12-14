import numpy as np


def create_curve(length, center, width):
    """
    Generates a reflection curve with 0 and 1 values.
    :param length: the total length of the curve to create
    :param center:  the center of the 1 values
    :param width: the width of the 1 values (will be applied in positive AND negative direction)
    """
    array = np.zeros([1, length])
    for i in range(length):
        # switch on elements around the center
        if (i >= center - width) & (i <= center + width):
            array[0, i] = 1

        # switch on elements at the end of the array?
        end = width - center
        if (end > 0) & (i >= length - end):
            array[0, i] = 1

        # switch on elements at the beginning of the array?
        begin = center + width - length
        if (begin > 0) & (i < begin):
            array[0, i] = 1

    return array[0]
