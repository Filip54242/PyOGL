import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from pyogl_gui.gui_base import GUIBase


class PyGameGui(GUIBase):
    def __init__(self, resolution: tuple = (800, 600), fov: float = 45, render_bounds: tuple = (0.1, 50)):
        super().__init__(resolution, fov, render_bounds)
        self.init_gui()

    def init_gui(self):
        pygame.init()
        pygame.display.set_mode(self.resolution, DOUBLEBUF | OPENGL)
        self.init_opengl()
        self.add_event(pygame.QUIT, self.quit)
        self.add_event(pygame.K_ESCAPE, self.quit)

    def clear_frame(self):
        pygame.display.flip()
        pygame.time.wait(10)

    def close(self):
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type in self.events.keys():
                self.events[event.type]()
            elif event.type == pygame.KEYDOWN and event.key in self.events.keys():
                self.events[event.key]()
