from gl_drawable.drawable_2d.polygon import Polygon
from gl_drawable.gl_drawable import GLDrawable
from math import sin, cos, pi
from OpenGL.GL import glBegin, glVertex3fv, glColor3fv, glEnd, GL_TRIANGLE_FAN


class UVSphere(GLDrawable):
    def __init__(self, center: tuple = (0, 0, 0), radius: float = 1, segments: int = 16, rings: int = 32,
                 color: tuple = None):
        super().__init__(color=color)
        self.center = center
        self.radius = radius
        self.segments = segments
        self.no_rings = rings
        self.rings = None
        self.top_point = None
        self.bottom_point = None
        self.compute_rings()
        self.compute_vertices()
        self.compute_edges()
        self.compute_surfaces()
        del self.rings

    def index_of_vertex(self, vertex):
        return self.vertices.index(vertex)

    def compute_rings(self):
        count = 1
        self.rings = []
        while count <= self.no_rings:
            center_vertex = list(self.center)
            coefficient = (pi / 2) - (pi * count) / self.no_rings

            center_vertex[2] += self.radius * sin(coefficient)
            current_radius = self.radius * cos(coefficient)

            self.rings.append(Polygon(tuple(center_vertex), current_radius, self.segments))

            count += 1

    def compute_edges(self):
        self.edges = []

        for ring in self.rings:
            for edge in ring.edges:
                first_vertex = ring.vertices[edge[0]]
                second_vertex = ring.vertices[edge[1]]
                self.edges.append([self.index_of_vertex(first_vertex), self.index_of_vertex(second_vertex)])

        for vertex in self.rings[0].vertices:
            self.edges.append([self.index_of_vertex(self.top_point), self.index_of_vertex(vertex)])

        for vertex in self.rings[-1].vertices:
            self.edges.append([self.index_of_vertex(self.bottom_point), self.index_of_vertex(vertex)])

        for ring_index in range(len(self.rings) - 1):
            for vertex_index in range(len(self.rings[ring_index].vertices)):
                first_vertex = self.rings[ring_index].vertices[vertex_index]
                second_vertex = self.rings[ring_index + 1].vertices[vertex_index]
                self.edges.append([self.index_of_vertex(first_vertex), self.index_of_vertex(second_vertex)])

    def compute_vertices(self):
        self.top_point = list(self.center)
        self.bottom_point = list(self.center)

        self.top_point[2] += self.radius
        self.bottom_point[2] -= self.radius

        self.vertices = [self.top_point, self.bottom_point]
        for ring in self.rings:
            self.vertices += ring.vertices

    def compute_surfaces(self):
        top_ring = []
        bottom_ring = []

        for vertex in self.rings[0].vertices:
            top_ring.append(self.index_of_vertex(vertex))
        for vertex in self.rings[-1].vertices:
            bottom_ring.append(self.index_of_vertex(vertex))

        self.surfaces = [top_ring, bottom_ring]

        for ring_index in range(len(self.rings) - 1):
            for vertex_index in range(len(self.rings[ring_index].vertices) - 1):
                first_vertex = self.index_of_vertex(self.rings[ring_index].vertices[vertex_index])
                second_vertex = self.index_of_vertex(self.rings[ring_index].vertices[vertex_index + 1])
                third_vertex = self.index_of_vertex(self.rings[ring_index + 1].vertices[vertex_index + 1])
                forth_vertex = self.index_of_vertex(self.rings[ring_index + 1].vertices[vertex_index])
                self.surfaces.append([first_vertex, second_vertex, third_vertex, forth_vertex])

            first_vertex = self.index_of_vertex(self.rings[ring_index].vertices[-1])
            second_vertex = self.index_of_vertex(self.rings[ring_index].vertices[0])
            third_vertex = self.index_of_vertex(self.rings[ring_index + 1].vertices[0])
            forth_vertex = self.index_of_vertex(self.rings[ring_index + 1].vertices[-1])
            self.surfaces.append([first_vertex, second_vertex, third_vertex, forth_vertex])

    def draw_top_circle(self):
        glBegin(GL_TRIANGLE_FAN)
        glVertex3fv(self.top_point)
        for vertex in self.surfaces[0]:
            glVertex3fv(self.vertices[vertex])
        glColor3fv(self.color)
        glEnd()

    def draw_bottom_circle(self):
        glBegin(GL_TRIANGLE_FAN)
        glVertex3fv(self.bottom_point)
        for vertex in self.surfaces[1]:
            glVertex3fv(self.vertices[vertex])
        glColor3fv(self.color)
        glEnd()

    def draw_surfaces(self):
        if self.color is not None:
            self.draw_top_circle()
            self.draw_bottom_circle()
            for index in range(2, len(self.surfaces)):
                self.draw_surface(self.surfaces[index])
