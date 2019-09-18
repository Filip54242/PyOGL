from gl_drawable import *
from Square import *
from Circle import *
from Cube import *

pygame.init()
display = (1280, 720)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50)
glTranslatef(0.0, 0.0, -3)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #sq = Square(axis=0)
    # sq = Circle(radius=1, segments=50, axis=1)
    sq = Cube(size=1)

    glRotatef(1, 1, 1, 0)
    sq.draw(color=(1, 0, 0))
    #sq.draw()


    pygame.display.flip()
    pygame.time.wait(100)
