from pyogl_gui.pygame_gui import PyGameGui
import gl_drawable.drawable_3d.sphere as sphere
import pygame

g = PyGameGui()

g.move_camera(-3, 2)


def rotate_right():
    g.rotate_camera(10, 1)


def rotate_left():
    g.rotate_camera(-10, 1)


def rotate_up():
    g.rotate_camera(10, 0)


def rotate_down():
    g.rotate_camera(-10, 0)


def zoom_in():
    g.move_camera(-1, 2)


def zoom_out():
    g.move_camera(1, 2)


g.add_event(pygame.K_LEFT, rotate_left)

g.add_event(pygame.K_UP, rotate_up)

g.add_event(pygame.K_DOWN, rotate_down)

g.add_event(pygame.K_RIGHT, rotate_right)

g.add_event(pygame.K_EQUALS, zoom_out)

g.add_event(pygame.K_MINUS, zoom_in)

obj1 = sphere.UVSphere()

g.add_object(obj1)

g.start()
