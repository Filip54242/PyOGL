from Square import *


class Cube(GLDrawable):

    def __init__(self, center: tuple = (0, 0, 0), size: float = 1):
        super().__init__()
        self.center = center
        self.size = size
        self.first_square = None
        self.second_square = None
        self.create_squares()
        self.compute_vertices()
        self.compute_edges()
        self.compute_surfaces()

    def first_square_idx(self, index):
        return self.vertices.index(self.first_square.vertices[index])

    def second_square_idx(self, index):
        return self.vertices.index(self.second_square.vertices[index])

    def create_squares(self):
        center_one = list(self.center)
        center_two = list(self.center)

        center_one[2] -= self.size / 2
        center_two[2] += self.size / 2

        self.first_square = Square(center=tuple(center_one))
        self.second_square = Square(center=tuple(center_two))

    def compute_surfaces(self):
        self.surfaces = self.first_square.surfaces.copy()
        for surface in self.second_square.surfaces:
            new_surface = []
            for vertex in surface:
                new_surface.append(self.second_square_idx(vertex))
            self.surfaces.append(new_surface)

        for index in range(len(self.second_square.vertices) - 1):
            self.surfaces.append([self.first_square_idx(index),
                                  self.first_square_idx(index + 1),
                                  self.second_square_idx(index + 1),
                                  self.second_square_idx(index)])

        self.surfaces.append([self.first_square_idx(-1), self.first_square_idx(0), self.second_square_idx(0),
                             self.second_square_idx(-1)])

    def compute_edges(self):
        self.edges = self.first_square.edges.copy()
        for edge in self.second_square.edges:
            new_edge = []
            for vertex in edge:
                new_edge.append(self.second_square_idx(vertex))
            self.edges.append(new_edge)

        for index in range(len(self.second_square.vertices)):
            self.edges.append([self.first_square_idx(index), self.second_square_idx(index)])

    def compute_vertices(self):
        self.vertices = self.first_square.vertices + self.second_square.vertices
