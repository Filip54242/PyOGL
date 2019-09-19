from Polygon import *


class Polyhedron(GLDrawable):

    def __init__(self, center: tuple = (0, 0, 0), size: float = 1, radius: float = 1, segments: int = 3):
        super().__init__()
        self.center = center
        self.size = size
        self.radius = radius
        self.segments = segments
        self.first_polygon = None
        self.second_polygon = None
        self.create_polygons()
        self.compute_vertices()
        self.compute_edges()
        self.compute_surfaces()

    def first_polygon_idx(self, index):
        return self.vertices.index(self.first_polygon.vertices[index])

    def second_polygon_idx(self, index):
        return self.vertices.index(self.second_polygon.vertices[index])

    def create_polygons(self):
        center_one = list(self.center)
        center_two = list(self.center)

        center_one[2] -= self.size / 2
        center_two[2] += self.size / 2

        self.first_polygon = Polygon(center=tuple(center_one), radius=self.radius, segments=self.segments)
        self.second_polygon = Polygon(center=tuple(center_two), radius=self.radius, segments=self.segments)

    def compute_surfaces(self):
        self.surfaces = self.first_polygon.surfaces.copy()
        for surface in self.second_polygon.surfaces:
            new_surface = []
            for vertex in surface:
                new_surface.append(self.second_polygon_idx(vertex))
            self.surfaces.append(new_surface)

        for index in range(len(self.second_polygon.vertices) - 1):
            self.surfaces.append([self.first_polygon_idx(index),
                                  self.first_polygon_idx(index + 1),
                                  self.second_polygon_idx(index + 1),
                                  self.second_polygon_idx(index)])

        self.surfaces.append([self.first_polygon_idx(-1), self.first_polygon_idx(0), self.second_polygon_idx(0),
                              self.second_polygon_idx(-1)])

    def compute_edges(self):
        self.edges = self.first_polygon.edges.copy()
        for edge in self.second_polygon.edges:
            new_edge = []
            for vertex in edge:
                new_edge.append(self.second_polygon_idx(vertex))
            self.edges.append(new_edge)

        for index in range(len(self.second_polygon.vertices)):
            self.edges.append([self.first_polygon_idx(index), self.second_polygon_idx(index)])

    def compute_vertices(self):
        self.vertices = self.first_polygon.vertices + self.second_polygon.vertices
