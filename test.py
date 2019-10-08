from OpenGL.GL import glTranslatef, glRotatef, glClear, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT
from OpenGL.raw.GLU import gluPerspective
from gl_drawable.drawable_3d.sphere import UVSphere
import pygame
from pygame.locals import DOUBLEBUF, OPENGL

pygame.init()
display = (1280, 720)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50)
glTranslatef(0.0, 0.0, -3)
glRotatef(90, 1, 0, 0)

sq = UVSphere(segments=4, color=(0,1,0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # sq = Square(axis=0)
    # sq = Circle(radius=1, segments=50, axis=1)
    # sq = Cube(size=1)
    glRotatef(1, 1, 0, 0)
    sq.rotate()
    sq.draw()
    # glRotatef(1, 1, 0, 0)
    # sq.draw(color=(1, 0, 0))
    # sq.rotate(angle=0.1, axis=2)

    pygame.display.flip()
    pygame.time.wait(10)
