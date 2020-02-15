from gl_drawable.drawable_2d.square import Square
from gl_drawable.drawable_3d.polyhedron import Polyhedron


class Cube(Polyhedron):

    def __init__(self, center: tuple = (0, 0, 0), size: float = 1, color: tuple = None):
        super().__init__(color=color)
        self.center = center
        self.size = size
        self.create_polygons()
        self.compute_vertices()
        self.compute_edges()
        self.compute_surfaces()

    def create_polygons(self):
        center_one = list(self.center)
        center_two = list(self.center)

        center_one[2] -= self.size / 2
        center_two[2] += self.size / 2

        self.first_polygon = Square(center=tuple(center_one), size=self.size)
        self.second_polygon = Square(center=tuple(center_two), size=self.size)
