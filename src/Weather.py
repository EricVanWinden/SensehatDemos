from sense_hat import SenseHat
from NumberMatrix import *
from time import sleep

sense = SenseHat()
sense.set_rotation(90)

print("Weather is shown on LED matrix. Press Ctrl-C to exit")
try:
    while True:
        t = int(sense.get_temperature())
        sense.show_letter("T")
        sleep(0.5)
        matrix = create_matrix(t)
        pixels = create_pixels(matrix)
        sense.set_pixels(pixels)
        sleep(0.5)

        rh = int(sense.get_humidity())
        sense.show_letter("H")
        sleep(0.5)
        matrix = create_matrix(rh)
        pixels = create_pixels(matrix)
        sense.set_pixels(pixels)
        sleep(0.5)
        
        p = int(sense.get_pressure())
        sense.show_message("p=" + str(p))

except KeyboardInterrupt:
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
    sense.set_pixels(pixels_off)
    print("Weather demo stopped")