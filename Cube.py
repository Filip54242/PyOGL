from Square import *
from Polyhedron import *


class Cube(Polyhedron):

    def __init__(self, center: tuple = (0, 0, 0), size: float = 1):
        super().__init__()
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
