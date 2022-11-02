from pygame import image, Surface


class Floor:
    surface = image.load('image/floor/floor.jpg')
    width, height = Surface.get_size(surface)
    speed = 2

    def __init__(self, screen):
        self.screen = screen
        self.x = 0

    def draw(self, is_play):
        if not is_play:
            return
        rect_01 = self.surface.get_rect(bottomleft=(self.x, self.screen.height))
        rect_02 = self.surface.get_rect(bottomleft=(self.x + self.width, self.screen.height))
        rect_03 = self.surface.get_rect(bottomleft=(self.x + self.width * 2, self.screen.height))

        self.screen.window.blit(self.surface, rect_01)
        self.screen.window.blit(self.surface, rect_02)
        self.screen.window.blit(self.surface, rect_03)

        if self.x <= -Floor.width:
            self.x = 0
        self.x -= Floor.speed
