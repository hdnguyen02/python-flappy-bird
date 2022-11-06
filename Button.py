from pygame import image


class Button:
    def __init__(self, x_center, y_center, surface, screen):
        self.screen = screen
        self.sf = surface
        self.rect = self.sf.get_rect(center=(x_center, y_center))

    def draw(self):
        self.screen.window.blit(self.sf, self.rect)

    def check_is_click(self,pos):
        x_pos,y_pos = pos
        if x_pos in range(self.rect.left,self.rect.right) and y_pos in range(self.rect.top,self.rect.bottom):
            return True
        return False

    def change_sf(self,new_sf):
        self.sf = new_sf
