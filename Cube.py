from Square import *


class Cube(GLDrawable):

    def __init__(self, center: tuple = (0, 0, 0), size: float = 1):
        super().__init__()
        self.center = center
        self.size = size

    def compute_surface(self):
        pass

    def compute_edges(self):
        pass

    def compute_vertices(self):
        pass
