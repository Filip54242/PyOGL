from gl_drawable import *
from Square import *
from Circle import *

pygame.init()
display = (1280, 720)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50)
glTranslatef(0.0, 0.0, -3)
while True:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    sq = Square(axis=1)
    #sq = Circle(radius=1, segments=10)

    sq.compute_vertices()
    sq.compute_edges()
    sq.compute_surface()
    #glRotatef(1, 1, 0, 0)
    sq.draw(color=(0, 1, 0))

    pygame.display.flip()
    pygame.time.wait(10)
