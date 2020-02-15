from tkinter import *
import pygame
import random
import os
from gl_drawable import gl_drawable
from gl_drawable.drawable_3d import *
from pyogl_gui.pygame_gui import PyGameGui


class TKGUI:
    def __init__(self):
        self.rotate_left_button = None
        self.rotate_right_button = None
        self.rotate_up_button = None
        self.rotate_down_button = None
        self.zoom_in_button = None
        self.zoom_out_botton = None
        self.py_game_gui = None
        self.main_window = None
        self.py_game_frame = None
        self.object_colors = [None, (0, 0, 1), (0, 1, 0), (1, 0, 0)]
        self.init_main_window()

    def init_main_window(self):
        self.main_window = Tk()
        self.py_game_frame = Frame(self.main_window, width=800, height=600)
        self.py_game_frame.grid(row=0, column=0, columnspan=5)
        self.main_window.update()
        os.environ['SDL_WINDOWID'] = str(self.py_game_frame.winfo_id())
        self.py_game_gui = PyGameGui()
        self.py_game_gui.move_camera(-3, 2)
        self.zoom_out_button = Button(self.main_window, text='Zoom Out', command=self.zoom_out)
        self.zoom_out_button.grid(row=1, column=0)
        self.zoom_in_button = Button(self.main_window, text='Zoom In', command=self.zoom_in)
        self.zoom_in_button.grid(row=1, column=4)
        self.rotate_left_button = Button(self.main_window, text='Rotate left', command=self.rotate_left)
        self.rotate_left_button.grid(row=3, column=1)
        self.rotate_right_button = Button(self.main_window, text='Rotate right', command=self.rotate_right)
        self.rotate_right_button.grid(row=3, column=3)
        self.rotate_up_button = Button(self.main_window, text='Rotate up', command=self.rotate_left)
        self.rotate_up_button.grid(row=2, column=2)
        self.rotate_down_button = Button(self.main_window, text='Rotate down', command=self.rotate_right)
        self.rotate_down_button.grid(row=4, column=2)

    def rotate_right(self):
        self.py_game_gui.rotate_camera(10, 1)

    def rotate_left(self):
        self.py_game_gui.rotate_camera(-10, 1)

    def rotate_up(self):
        self.py_game_gui.rotate_camera(10, 0)

    def rotate_down(self):
        self.py_game_gui.rotate_camera(-10, 0)

    def zoom_in(self):
        self.py_game_gui.move_camera(1, 2)

    def zoom_out(self):
        self.py_game_gui.rotate_camera(-1, 2)

    def complexity_object(self, object: int, operation: float):

        if object is gl_drawable:
            pass

    def main_loop(self):
        while True:
            self.py_game_gui.handle_frame()
            self.main_window.update()
