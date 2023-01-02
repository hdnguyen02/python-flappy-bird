from pygame import image, transform, Surface, USEREVENT, time, init, mixer
from Utilitie import Utilitie

mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
init()


class Bird:
    gravity = 0.25
    speed = 5
    bird_fly = USEREVENT + 5
    time.set_timer(bird_fly, 16)

    X = 140 # tọa độ X của chim

    sound_space_click = mixer.Sound('sound/nhay.mp3')
    sound_collision = mixer.Sound('sound/vacham.mp3')
    sound_die = mixer.Sound('sound/thua.mp3')

    def __init__(self, screen):
        self.screen = screen
        self.index_surface = 0
        self.list_surface = []
        self.add_list_surface()
        self.surface = self.list_surface[self.index_surface]
        self.rect = self.surface.get_rect(topleft=(140, self.screen.height / 2))
        self.movement = 0
        # màn hình start game
        self.sf_title_game = Utilitie.surface_scale('image/title.png', 14)
        self.rbird_start = self.surface.get_rect(midleft=(370, 180))

    @property
    def getXBird(self):
        return self.list_surface[0]

    def draw_game_start(self):
        rect_title = self.sf_title_game.get_rect(midleft=(70, 180))
        self.screen.window.blit(self.sf_title_game, rect_title)
        self.screen.window.blit(self.surface, self.rbird_start)

    def animation(self):
        self.surface = self.list_surface[self.index_surface]
        self.rect = self.surface.get_rect(center=(Bird.X, self.rect.centery))

    def add_list_surface(self):
        for i in range(17):
            temp = image.load('image/bird/' + str(i) + '.jpg')
            w, h = Surface.get_size(temp)
            temp = transform.scale(temp, (w / 17, h / 17))
            self.list_surface.append(temp)


    @property
    def getY(self):
        return self.rect.y

    def handle_click_and_mouse(self):
        self.movement = 0
        self.movement = -Bird.speed

    def reset_game(self):
        self.rect = self.surface.get_rect(center=(Bird.X, self.screen.height // 2))
        self.movement = 0

    def isCcollision(self, rCols):  # return về True nếu con chim đã va chạm
        for rCol in rCols:
            if self.rect.colliderect(rCol["bottom"]) or self.rect.colliderect(rCol["top"]):
                return True
            return False

    def draw_handle_game(self):
        self.movement += Bird.gravity
        self.rect.centery += self.movement
        self.screen.window.blit(self.surface, self.rect)

    def event_fly(self, event):
        if event.type == Bird.bird_fly:
            if self.index_surface < 16:
                self.index_surface += 1
            else:
                self.index_surface = 0
            self.animation()
