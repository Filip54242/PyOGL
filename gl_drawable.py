import abc
from random import randint
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from math import cos, sin, radians, pi, degrees


class GLDrawable:
    AXIS = {0: (0, 1), 1: (0, 2), 2: (1, 2)}

    def __init__(self, vertices: list = None, edges: list = None, surfaces: list = None):
        self.vertices = vertices
        self.edges = edges
        self.surfaces = surfaces

    def draw_edges(self):
        assert self.edges is not None, "No edge data!"
        assert self.vertices is not None, "No vertices data!"

        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def draw_surface(self, surface: list, color: tuple):
        assert surface is not None, "No surface data!"
        assert color is not None, "No color for the surface!"
        glBegin(GL_POLYGON)
        for vertex in surface:
            glVertex3fv(self.vertices[vertex])
        # glColor3fv((randint(0, 1), randint(0, 1), randint(0, 1)))
        glColor3fv(color)
        glEnd()

    def draw_surfaces(self, color: tuple):
        assert color is not None, "No color for the surfaces!"
        for surface in self.surfaces:
            self.draw_surface(surface, color)

    def draw(self, color: tuple = None):
        if color is not None:
            self.draw_surfaces(color)
        self.draw_edges()

    def rotate(self, axis: int = 0, angle: float = 0):
        assert -1 < axis < 3, "Invalid axis!"
        axis = self.AXIS[axis]
        new_vertices = []
        for vertex in self.vertices:
            new_vertex = list(vertex)

            first_value = new_vertex[axis[0]]
            second_value = new_vertex[axis[1]]

            new_vertex[axis[0]] = first_value * cos(radians(angle)) - second_value * sin(radians(angle))
            new_vertex[axis[1]] = first_value * sin(radians(angle)) + second_value * cos(radians(angle))

            new_vertices.append(tuple(new_vertex))

        self.vertices = new_vertices

    @abc.abstractmethod
    def compute_surfaces(self):
        pass

    @abc.abstractmethod
    def compute_edges(self):
        pass

    @abc.abstractmethod
    def compute_vertices(self):
        pass
