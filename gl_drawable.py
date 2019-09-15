import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class GLDrawable:
    def __init__(self, vertices: tuple = None, edges: tuple = None, surfaces: tuple = None):
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

    def draw_surface(self, surface: tuple = None, color: tuple = None):
        assert surface is not None, "No surface data!"
        glBegin(GL_QUADS)
        if color is not None:
            glColor3fv(color)
            for vertex in surface:
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def draw_surfaces(self, color: tuple = None):
        for surface in self.surfaces:
            self.draw_surface(surface, color)

    def draw(self):
        self.draw_edges()
        self.draw_surfaces()
    