from Polygon import *


class UVSphere(GLDrawable):
    def __init__(self, center: tuple = (0, 0, 0), radius: float = 1, segments: int = 16, rings: int = 32):
        super().__init__()
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

    def index_of_vertex(self, vertex):
        return self.vertices.index(vertex)

    def compute_rings(self):
        top_rings = []
        bottom_rings = []

        self.top_point = list(self.center)
        self.bottom_point = list(self.center)

        self.top_point[2] += self.radius
        self.bottom_point[2] -= self.radius

        step = self.radius / (self.no_rings // 2)
        current_step = 0
        current_radius = self.radius
        if self.no_rings % 2 == 1:
            ring = Polygon(self.center, current_radius, self.segments)
            current_radius -= step
            top_rings.append(ring)
            current_step = step
        else:
            current_step = step / 2

        for index in range(self.no_rings // 2):
            top_node = list(self.center)
            bottom_node = list(self.center)

            top_node[2] += current_step
            bottom_node[2] -= current_step

            top_rings.append(Polygon(tuple(top_node), current_radius, self.segments))
            bottom_rings.append(Polygon(tuple(bottom_node), current_radius, self.segments))

            current_step += step
            current_radius -= step

            top_rings.reverse()

        self.rings = top_rings + bottom_rings

    def compute_surfaces(self):
        pass

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

        for ring_index in range(len(self.rings)-1):
            for vertex_index in range(len(self.rings[ring_index].vertices)):
                first_vertex = self.rings[ring_index].vertices[vertex_index]
                second_vertex = self.rings[ring_index + 1].vertices[vertex_index]
                self.edges.append([self.index_of_vertex(first_vertex), self.index_of_vertex(second_vertex)])

    def compute_vertices(self):
        self.vertices = [self.top_point, self.bottom_point]
        for ring in self.rings:
            self.vertices += ring.vertices
