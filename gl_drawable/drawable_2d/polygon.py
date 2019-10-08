from gl_drawable.gl_drawable import GLDrawable
from math import sin, cos, radians
from OpenGL.GL import glBegin, glVertex3fv, glColor3fv, glEnd, GL_TRIANGLE_FAN


class Polygon(GLDrawable):
    def __init__(self, center: tuple = (0, 0, 0), radius: float = 1, segments: int = 10, axis: int = 0,color: tuple = None):
        super().__init__(color=color)
        assert -1 < axis < 3, "Invalid axis!"
        self.center = center
        self.radius = radius
        self.segments = segments
        self.axis = self.AXIS[axis]
        self.compute_vertices()
        self.compute_edges()
        self.compute_surfaces()

    def compute_vertices(self):
        self.vertices = []
        step = 360 / self.segments
        angle = 0
        while angle <= 360:
            current_point = list(self.center)
            current_point[self.axis[0]] += self.radius * cos(radians(angle))
            current_point[self.axis[1]] += self.radius * sin(radians(angle))
            self.vertices.append(tuple(current_point))
            angle += step

    def compute_edges(self):
        self.edges = [[index - 1, index] for index in range(1, len(self.vertices))]

    def compute_surfaces(self):
        self.surfaces = [[index for index in range(len(self.vertices))]]

    def draw_surfaces(self):
        if self.color is not None:
            glBegin(GL_TRIANGLE_FAN)
            glVertex3fv(self.center)
            for surface in self.surfaces:
                for vertex in surface:
                    glVertex3fv(self.vertices[vertex])
            glColor3fv(self.color)
            glEnd()
