from gl_drawable import GLDrawable


class Square(GLDrawable):
    def __init__(self, center: tuple, size: int):
        super().__init__()
        self.center = center
        self.size = size

    def compute_vertices(self):
        first_point = [self.center[0], self.center[1], self.center[2]]

        first_point[0] -= self.size / 2
        first_point[1] -= self.size / 2

        first_point = tuple(first_point)

        second_point = (first_point[0] + self.size, first_point[1], first_point[2])
        third_point = (first_point[0], first_point[1] + self.size, first_point[2])
        forth_point = (third_point[0] + self.size, third_point[1], third_point[2])

        super().vertices = (first_point, second_point, third_point, forth_point)

    def compute_edges(self):
        super().edges = ((0, 1), (0, 2), (1, 3), (2, 3))

