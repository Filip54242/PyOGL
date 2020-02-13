from tkinter import *
import pygame
import random
import os

from gl_drawable.drawable_3d import sphere
from pyogl_gui.pygame_gui import PyGameGui

root = Tk()
embed = Frame(root, width=640, height=480)
embed.grid(row=0, column=0, columnspan=4)
root.update()
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

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
    g.move_camera(1, 2)


def zoom_out():
    g.move_camera(-1, 2)


g.add_event(pygame.K_LEFT, rotate_left)

g.add_event(pygame.K_UP, rotate_up)

g.add_event(pygame.K_DOWN, rotate_down)

g.add_event(pygame.K_RIGHT, rotate_right)

g.add_event(pygame.K_EQUALS, zoom_out)

g.add_event(pygame.K_MINUS, zoom_in)

obj1 = sphere.UVSphere()

g.add_object(obj1)

zoom_out_button = Button(root, text='Zoom Out', command=zoom_out)
zoom_out_button.grid(row=1, column=0)
zoom_in_button = Button(root, text='Zoom In', command=zoom_in)
zoom_in_button.grid(row=1, column=1)
rotate_left_button = Button(root, text='Rotate left', command=rotate_left)
rotate_left_button.grid(row=1, column=2)
rotate_right_button = Button(root, text='Rotate right', command=rotate_right)
rotate_right_button.grid(row=1, column=3)
while True:
    # your code here
    g.handle_frame()
    root.update()
