from gl_drawable import *
from math import cos, sin, radians


class Circle(GLDrawable):
    def __init__(self, center: tuple = (0, 0, 0), radius: float = 1, segments: int = 10):
        super().__init__()
        self.center = center
        self.radius = radius
        self.segments = segments

    def compute_vertices(self):
        self.vertices = []
        step = 360 / self.segments
        angle = 0
        while angle <= 360:
            current_point = list(self.center)
            current_point[0] += self.radius * cos(radians(angle))
            current_point[1] += self.radius * sin(radians(angle))
            self.vertices.append(tuple(current_point))
            angle += step

    def compute_edges(self):
        self.edges = [[index - 1, index] for index in range(1, len(self.vertices))]

    def compute_surface(self):
        self.surfaces = [[index for index in range(len(self.vertices))]]

    def draw_surfaces(self, color: tuple):
        assert color is not None, "No color for the surfaces!"
        glBegin(GL_TRIANGLE_FAN)
        glVertex3fv(self.center)
        for surface in self.surfaces:
            for vertex in surface:
                glVertex3fv(self.vertices[vertex])
        glColor3fv(color)
        glEnd()
