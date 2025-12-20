from number_matrix import NumberMatrix


class SandBox:
    def __init__(self):
        self.nm = NumberMatrix()

    def run(self):
        matrix = self.nm.make_gradient_3d()
        pixels_v1 = self.nm.create_pixels(matrix)
        print(pixels_v1)


if __name__ == "__main__":
    demo = SandBox()
    demo.run()
