
from View import Screen
from pygame import image, Surface

# nêu thay đổi : chỉ thay đổi background, chim
# còn cột và sàn là cố định



class Floor:
    surface = image.load('image/floor/floor.jpg')
    width = Surface.get_width(surface)
    height = Surface.get_height(surface)
    speed = 2

    def __init__(self):
        self.x = 0

    def draw(self, screen, is_play):
        if not is_play:
            return
        rect_01 = self.surface.get_rect(bottomleft=(self.x, Screen.height))
        rect_02 = self.surface.get_rect(bottomleft=(self.x + self.width, Screen.height))
        rect_03 = self.surface.get_rect(bottomleft=(self.x + self.width * 2, Screen.height))

        screen.blit(self.surface, rect_01)
        screen.blit(self.surface, rect_02)
        screen.blit(self.surface, rect_03)

        if self.x <= -Floor.width:
            self.x = 0
        self.x -= Floor.speed
