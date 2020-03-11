from tkinter import *
import os
from pyogl_gui.pygame_gui import PyGameGui
from gl_drawable.utils import *
from random import randint


class TKGUI:
    COMPLEXITIES = {str(Cube()): cube_complexity, str(Polyhedron()): polyhedron_complexity,
                    str(Polygon()): polygon_complexity, str(UVSphere()): sphere_complexity,
                    str(Square()): square_complexity}
    OBJECTS = [Cube, Polyhedron, Polygon, UVSphere, Square]
    COLORS = [None, (0, 0, 1), (0, 1, 0), (1, 0, 0)]

    def __init__(self):
        self.rotate_left_button = None
        self.rotate_right_button = None
        self.rotate_up_button = None
        self.rotate_down_button = None
        self.zoom_in_button = None
        self.zoom_out_botton = None
        self.complexity_plus_button = None
        self.complexity_minus_button = None
        self.change_color_button = None
        self.change_object_button = None
        self.close_button = None

        self.py_game_gui = None
        self.main_window = None
        self.py_game_frame = None
        self.main_object = None
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
        self.rotate_up_button = Button(self.main_window, text='Rotate up', command=self.rotate_up)
        self.rotate_up_button.grid(row=2, column=2)
        self.rotate_down_button = Button(self.main_window, text='Rotate down', command=self.rotate_down)
        self.rotate_down_button.grid(row=4, column=2)
        self.complexity_plus_button = Button(self.main_window, text='Complexity +', command=self.complexity_plus)
        self.complexity_plus_button.grid(row=5, column=0)
        self.complexity_minus_button = Button(self.main_window, text='Complexity -', command=self.complexity_minus)
        self.complexity_minus_button.grid(row=5, column=4)
        self.change_color_button = Button(self.main_window, text='Color', command=self.change_color)
        self.change_color_button.grid(row=5, column=1)
        self.change_object_button = Button(self.main_window, text='Object', command=self.change_object)
        self.change_object_button.grid(row=5, column=3)
        self.close_button = Button(self.main_window, text='Quit', command=self.quit)
        self.close_button.grid(row=7, column=4)

    def quit(self):
        self.py_game_gui.close()
        self.main_window.quit()

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

    def change_object(self):
        self.main_object = self.OBJECTS[randint(0, len(self.OBJECTS) - 1)]()
        self.update_rendered_object()

    def change_color(self):
        self.main_object.color = self.COLORS[randint(0, len(self.COLORS) - 1)]
        self.update_rendered_object()

    def complexity_plus(self):
        self.complexity_object(0.5)

    def complexity_minus(self):
        self.complexity_object(-0.5)

    def update_rendered_object(self):
        self.py_game_gui.objects.clear()
        self.py_game_gui.objects.append(self.main_object)

    def complexity_object(self, percentage):
        self.main_object = self.COMPLEXITIES[str(self.main_object)](self.main_object, percentage)
        self.update_rendered_object()

    def main_loop(self):
        while True:
            self.py_game_gui.handle_frame()
            self.main_window.update()
