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

    def draw_surface(self,surface: tuple, color: tuple):
        assert surface is not None, "No surface data!"
        assert color is not None, "No color for the surface!"
        glBegin(GL_QUADS)
        for vertex in surface:
            glVertex3fv(self.vertices[vertex])
            glColor3fv(color)
        glEnd()

    def draw_surfaces(self, color: tuple):
        assert color is not None, "No color for the surfaces!"
        if type(self.surfaces[0]) is tuple:
            for surface in self.surfaces:
                self.draw_surface(surface, color)
        else:
            self.draw_surface(self.surfaces, color)

    def draw(self, color: tuple = None):
        # if color is not None:
        #     self.draw_surfaces(color)

        self.draw_edges()

