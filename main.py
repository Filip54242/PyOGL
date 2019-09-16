import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)
surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)


def make_cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv((randint(0, 1), randint(0, 1), randint(0, 1)))
            glVertex3fv(vertices[vertex])
        break
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    rotate_angle = 0
    rotate_x = 0
    rotate_y = 0
    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_p:
                    rotate_angle += -0.2
                if event.key == K_m:
                    rotate_angle += 0.2
                if event.key == K_UP:
                    rotate_x += 0.2
                if event.key == K_DOWN:
                    rotate_x -= 0.2
                if event.key == K_RIGHT:
                    rotate_y += 0.2
                if event.key == K_LEFT:
                    rotate_y -= 0.2

        glRotatef(rotate_angle, rotate_x, rotate_y, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        make_cube()
        pygame.display.flip()
        pygame.time.wait(1000)


main()
