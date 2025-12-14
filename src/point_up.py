from sense_hat import SenseHat
from NumberMatrix import *

sense = SenseHat()
off = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]


def set_arrow(off, on):
    matrix = np.array([
        [off, off, off, on, on, off, off, off],
        [off, off, on, on, on, on, off, off],
        [off, on, on, on, on, on, on, off],
        [on, on, on, on, on, on, on, on],
        [off, off, off, on, on, off, off, off],
        [off, off, off, on, on, off, off, off],
        [off, off, off, on, on, off, off, off],
        [off, off, off, on, on, off, off, off],
    ])
    pixels = create_pixels(matrix)
    sense.set_pixels(pixels)


print("Accelerometer, arrow is pointing up. Press Ctrl-C to exit")
try:
    while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        maximum = max(abs(x), abs(y), abs(z))
        if maximum > 1:
            set_arrow(off, red)
        else:
            set_arrow(off, white)

        x = round(x, 0)
        y = round(y, 0)
        z = round(z, 0)

        print(str(x) + " " + str(y) + " " + str(x) + " " + str(max))

        # Update the rotation of the display depending on which way up the Sense HAT is
        if x == -1:
            sense.set_rotation(180)
        elif y == 1:
            sense.set_rotation(90)
        elif y == -1:
            sense.set_rotation(270)
        else:
            sense.set_rotation(0)

except KeyboardInterrupt:
    set_arrow(off, off)
    print("Point up stopped")
