from sense_hat import SenseHat

class Joystick:
    def __init__(self):
        off = [0, 0, 0]
        self.pixels_off = [
            off, off, off, off, off, off, off, off,
            off, off, off, off, off, off, off, off,
            off, off, off, off, off, off, off, off,
            off, off, off, off, off, off, off, off,
            off, off, off, off, off, off, off, off,
            off, off, off, off, off, off, off, off,
            off, off, off, off, off, off, off, off,
            off, off, off, off, off, off, off, off]

    def run(self):
        # initialize
        sense = SenseHat()
        color = [255, 255, 255]
        x = 4
        y = 4
        sense.set_pixels(self.pixels_off)
        sense.set_pixel(x, y, color)
        busy = True

        print("Use joystick to move the dot. Hold middle to stop")
        while busy:
            for event in sense.stick.get_events():
                if (event.direction == 'middle') & (event.action == 'held'):
                    busy = False

                if (event.action == 'pressed') | (event.action == 'held'):
                    if event.direction == 'up':
                        if y > 0:
                            y -= 1
                            color = [0, 255, 0]
                        else:
                            color = [255, 0, 0]

                    if event.direction == 'down':
                        if y < 7:
                            y += 1
                            color = [0, 255, 0]
                        else:
                            color = [255, 0, 0]

                    if event.direction == 'left':
                        if x > 0:
                            x -= 1
                            color = [0, 255, 0]
                        else:
                            color = [255, 0, 0]

                    if event.direction == 'right':
                        if x < 7:
                            x += 1
                            color = [0, 255, 0]
                        else:
                            color = [255, 0, 0]

                if event.action == 'released':
                    color = [255, 255, 255]

                print(str(event.action) + " " + str(event.direction) + " " + str(x) + " " + str(y))
                sense.set_pixels(self.pixels_off)
                sense.set_pixel(x, y, color)

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
        print("Joystick demo stopped")