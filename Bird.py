from View import Screen
from Floor import Floor
from pygame import image, transform, Surface, K_SPACE, MOUSEBUTTONDOWN, KEYDOWN


class Bird(Screen):
    gravity = 0.25
    speed = 5  # tốc độ chim đi lên.

    def __init__(self, path_image='image/skeleton-01_fly_00.png'):
        self.surface = image.load(path_image)
        self.width, self.height = Surface.get_size(self.surface)

        self.surface = transform.scale(self.surface, (self.width / 4, self.height / 4))

        self.rect = self.surface.get_rect(center=(100, Screen.height / 2))
        self.movement = 0

    def handle_click_and_mouse(self):
        self.movement = 0
        self.movement = -Bird.speed

    def reset_game(self):
        self.rect = self.surface.get_rect(center=(100, Screen.height / 2))
        self.movement = 0

    def is_collision(self, pipe):  # return về True nếu con chim đã va chạm
        for sub_pipe in pipe.list_pipe:
            if self.rect.colliderect(sub_pipe):
                return True
        if self.rect.top <= 0 or self.rect.bottom >= Screen.height - Floor.height:
            return True
        return False

    def draw(self, window, is_play):
        if not is_play:
            return
        self.movement += Bird.gravity
        self.rect.centery += self.movement
        window.blit(self.surface, self.rect)

        # kiem tra va cham
