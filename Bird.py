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

        # kiểm tra xem game còn chạy hay không
        self.__is_play = True

    # setter getter
    @property
    def is_play(self):
        return self.__is_play

    @is_play.setter
    def is_play(self, status):
        self.__is_play = status

    def handle_event(self, sub_event):
        if ((sub_event.type == KEYDOWN and sub_event.key == K_SPACE) or (sub_event.type == MOUSEBUTTONDOWN)) and self.__is_play:
            self.movement = 0
            self.movement = -Bird.speed
        elif ((sub_event.type == KEYDOWN and sub_event.key == K_SPACE) or (sub_event.type == MOUSEBUTTONDOWN)) and not self.__is_play:
            self.reset_game()

    def reset_game(self):
        # điều chỉnh lại
        self.__is_play = True # set lại trạng thái của chú chim
        self.rect = self.surface.get_rect(center=(100, Screen.height / 2))
        self.movement = 0

    def is_collision(self, pipe):  # return về True nếu con chim đã va chạm
        for sub_pipe in pipe.list_pipe:
            if self.rect.colliderect(sub_pipe):
                return True
        if self.rect.top <= 0 or self.rect.bottom >= Screen.height - Floor.height:
            return True
        return False

    def draw(self, window):
        if not self.__is_play:
            return
        self.movement += Bird.gravity
        self.rect.centery += self.movement
        window.blit(self.surface, self.rect)



        # kiem tra va cham
