from Polygon import *


class Cylinder(GLDrawable):
    def __init__(self, center: tuple = (0, 0, 0), radius: float = 1, segments: int = 10, length: int = 1):
        super().__init__()
        self.center = center
        self.radius = radius
        self.segments = segments
        self.length = length
        self.first_circle=None

    def compute_surfaces(self):
        pass

    def compute_edges(self):
        pass

    def compute_vertices(self):
        pass
