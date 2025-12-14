from sense_hat import SenseHat
from NumberMatrix import *


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


sense = SenseHat()
on = [255, 255, 255]
off = [0, 0, 0]
pixels_off = [
    off, off, off, off, off, off, off, off,
    off, off, off, off, off, off, off, off,
    off, off, off, off, off, off, off, off,
    off, off, off, off, off, off, off, off,
    off, off, off, off, off, off, off, off,
    off, off, off, off, off, off, off, off,
    off, off, off, off, off, off, off, off,
    off, off, off, off, off, off, off, off]

print("Compass, dot is pointing north. Press Ctrl-C to exit")
try:
    while True:
        sense = SenseHat()
        north = sense.get_compass()
        coordinate = calculate_coordinate(north)
        sense.set_pixels(pixels_off)
        for j in range(coordinate.__len__()):
            sense.set_pixel(coordinate[j][0], coordinate[j][1], on)

except KeyboardInterrupt:
    sense.set_pixels(pixels_off)
    print("Compass stopped")
