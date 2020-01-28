from OpenGL.GL import glTranslatef, glRotatef, glClear, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT
from OpenGL.raw.GLU import gluPerspective
from gl_drawable import gl_drawable
import abc


class GUIBase:
    def __init__(self, resolution: tuple = (800, 600), fov: float = 45, render_bounds: tuple = (0.1, 50)):
        self.resolution = resolution
        self.fov = fov
        self.inferior_bound = render_bounds[0]
        self.superior_bound = render_bounds[1]
        self.objects = []
        self.events = {}

    def move_camera(self, amount: float = 0, axis: int = 0):
        assert -1 < axis < 3, "Invalid axis!"

        xyz = [0, 0, 0]
        xyz[axis] = amount
        x, y, z = xyz

        glTranslatef(x, y, z)

    def rotate_camera(self, angle: float = 0, axis: int = 0):
        assert -1 < axis < 3, "Invalid axis!"

        xyz = [0, 0, 0]
        xyz[axis] = 1
        x, y, z = xyz

        glRotatef(angle, x, y, z)

    def init_opengl(self):
        width, height = self.resolution
        gluPerspective(self.fov, (width / height), self.inferior_bound, self.superior_bound)

    def clear_opengl(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    @abc.abstractmethod
    def init_gui(self):
        pass

    def add_object(self, object: gl_drawable):
        self.objects.append(object)

    def add_event(self, event, action):
        self.events[event] = action

    @abc.abstractmethod
    def clear_frame(self):
        pass

    @abc.abstractmethod
    def handle_events(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    def quit(self):
        self.close()
        exit(0)

    def start(self):
        while True:
            self.clear_opengl()
            [object.draw() for object in self.objects]
            self.handle_events()
            self.clear_frame()
