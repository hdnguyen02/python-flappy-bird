from pygame import display



class Screen:
    def __init__(self, size):
        self.width, self.height = size
        self.size = size
        self.window = display.set_mode(self.size)


    def draw_window(self, surface, coordinate):
        self.window.blit(surface, coordinate)

    def x_center(self, surface):
        w = surface.get_width()
        return self.width / 2 -  w / 2
