from time import sleep
from sense_hat import SenseHat
from NumberMatrix import *

sense = SenseHat()

print("Counting down from 99 to 0 on LED matrix")
for i in range(101):
    matrix = create_matrix(99 - i)
    print_matrix(matrix)
    pixels = create_pixels(matrix)
    sense.set_pixels(pixels)
    sleep(0.5)
