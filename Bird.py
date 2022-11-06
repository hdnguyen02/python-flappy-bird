from Floor import Floor
from pygame import image, transform, Surface, USEREVENT, time,init, mixer
mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
init()


class Bird:
    gravity = 0.25
    speed = 5
    bird_fly = USEREVENT + 5
    time.set_timer(bird_fly, 16)

    centerx = 140

    sound_space_click = mixer.Sound('sound/nhay.mp3')
    sound_collision = mixer.Sound('sound/vacham.mp3')
    sound_die = mixer.Sound('sound/thua.mp3')

    def __init__(self, screen):
        self.screen = screen
        self.list_surface = []
        self.add_list_surface()
        self.index_surface = 0
        self.surface = self.list_surface[self.index_surface]
        self.rect = self.surface.get_rect(center=(Bird.centerx, self.screen.height / 2))
        self.movement = 0
        self.rect_start = self.surface.get_rect(midleft=(370, 180))
        self.sf_title_start = image.load('image/title.png')
        w_title, h_title = self.sf_title_start.get_size()

        self.sf_title_start = transform.scale(self.sf_title_start,(w_title / 14,h_title / 14))

        # tạo hiệu ứng chim bay.

    def draw_game_start(self):
        rect_title = self.sf_title_start.get_rect(midleft=(70,180))
        self.screen.window.blit(self.sf_title_start,rect_title)
        self.screen.window.blit(self.surface,self.rect_start)


    def animation(self):
        self.surface = self.list_surface[self.index_surface]
        self.rect = self.surface.get_rect(center=(Bird.centerx, self.rect.centery))

    def add_list_surface(self):
        for i in range(17):
            temp = image.load('image/bird/' + str(i) + '.jpg')
            w, h = Surface.get_size(temp)
            temp = transform.scale(temp, (w / 17, h / 17))
            self.list_surface.append(temp)

    def rotate(self):
        return transform.rotate(self.surface, -self.movement * 2)

    def handle_click_and_mouse(self):
        self.movement = 0
        self.movement = -Bird.speed

    def reset_game(self):
        self.rect = self.surface.get_rect(center=(self.centerx, self.screen.height // 2))
        self.movement = 0

    def is_collision(self, pipe):  # return về True nếu con chim đã va chạm
        for pipe in pipe.queue_pipe.queue:
            if self.rect.colliderect(pipe["rect_pipe_top"]) or self.rect.colliderect(pipe["rect_pipe_bottom"]):
                return True
        if self.rect.top <= 0 or self.rect.bottom >= self.screen.height - Floor.height:
            return True
        return False

    def draw_handle_game(self, is_play):
        if not is_play:
            return
        self.movement += Bird.gravity
        bird_rotate = self.rotate()
        self.rect.centery += self.movement
        self.screen.window.blit(bird_rotate, self.rect)


# làm tính năng chọn random chim và background + pipe

