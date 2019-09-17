from gl_drawable import *


class Square(GLDrawable):
    def __init__(self, center: tuple = (0, 0, 0), size: float = 1, vertices: list = None, axis: int = 0):
        super().__init__(vertices=vertices)
        assert -1 < axis < 3, "Invalid axis!"
        self.center = center
        self.size = size
        self.axis = self.AXIS[axis]

    def compute_vertices(self):
        first_point = list(self.center)

        first_point[self.axis[0]] -= self.size / 2
        first_point[self.axis[1]] -= self.size / 2

        second_point, third_point = first_point.copy(), first_point.copy()

        second_point[self.axis[0]] += self.size
        third_point[self.axis[1]] += self.size

        forth_point = third_point.copy()

        forth_point[self.axis[0]] += self.size

        self.vertices = [tuple(first_point), tuple(second_point), tuple(third_point), tuple(forth_point)]

    def compute_edges(self):
        self.edges = [[0, 1], [0, 2], [1, 3], [2, 3]]

    def compute_surface(self):
        self.surfaces = [[index for index in range(len(self.vertices))]]
