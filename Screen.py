from pygame import display
from pygame_gui import UIManager


class Screen:
    def __init__(self, size):
        self.width, self.height = size
        self.size = size
        self.window = display.set_mode(self.size)
        self.manager = UIManager(self.size)
