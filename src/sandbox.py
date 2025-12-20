from number_matrix import NumberMatrix


class SandBox:
    def __init__(self):
        self.nm = NumberMatrix()

    def run(self):
        matrix = self.nm.make_gradient_3d()
        rotations = [0,90]
        for rotation in rotations:
            self.nm.direction = rotation
            pixels_v1 = self.nm.create_pixels(matrix)
            print(pixels_v1)


if __name__ == "__main__":
    demo = SandBox()
    demo.run()
