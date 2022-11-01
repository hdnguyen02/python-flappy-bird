from View import Screen
from Floor import Floor
from pygame import image, transform, Surface, USEREVENT, time


# Điều chỉnh class Bird


class Bird:
    __gravity = 0.25
    __speed = 5
    bird_fly = USEREVENT + 1
    time.set_timer(bird_fly, 16)
    # tọa đô x center x của chim


    def __init__(self):
        self.centerx = 140
        self.list_surface = []
        self.add_list_surface()
        self.index_surface = 0
        self.surface = self.list_surface[self.index_surface]
        self.rect = self.surface.get_rect(center=(self.centerx , Screen.height / 2))
        self.movement = 0

        # tạo hiệu ứng chim bay.
    def animation(self):
        self.surface = self.list_surface[self.index_surface]
        self.rect = self.surface.get_rect(center=(self.centerx, self.rect.centery))

    def add_list_surface(self):
        for i in range(17):
            temp = image.load('image/bird/' + str(i) + '.jpg')
            w, h = Surface.get_size(temp)
            temp = transform.scale(temp, (w / 15, h / 15))
            self.list_surface.append(temp)

    def rotate(self):
        return transform.rotate(self.surface, -self.movement * 2)

    def handle_click_and_mouse(self):
        self.movement = 0
        self.movement = -Bird.__speed

    def reset_game(self):
        self.rect = self.surface.get_rect(center=(self.centerx, Screen.height / 2))
        self.movement = 0

    def is_collision(self, pipe):  # return về True nếu con chim đã va chạm
        for pipe in pipe.queue_pipe.queue:
            if self.rect.colliderect(pipe["rect_pipe_top"]):
                return True
            elif self.rect.colliderect(pipe["rect_pipe_bottom"]):
                return True
        if self.rect.top <= 0 or self.rect.bottom >= Screen.height - Floor.height:
            return True
        return False

    def draw(self, window, is_play):
        if not is_play:
            return
        self.movement += Bird.__gravity
        bird_rotate = self.rotate()
        self.rect.centery += self.movement
        window.blit(bird_rotate, self.rect)

        # kiem tra va cham
