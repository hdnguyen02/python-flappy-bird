from pygame import image, transform, Surface, USEREVENT, time, init, mixer
from Utilitie import Utilitie
from Floor import Floor

mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
init()


class Bird:
    GRAVITY = 0.25
    SPEED = 5
    eventBirdFly = USEREVENT + 5
    time.set_timer(eventBirdFly, 16)

    X = 140  # tọa độ X của chim

    soundJump = mixer.Sound('sound/nhay.mp3')
    soundCollision = mixer.Sound('sound/vacham.mp3')
    soundDie = mixer.Sound('sound/thua.mp3')

    def __init__(self, screen):
        self.screen = screen
        self.index_surface = 0
        self.list_surface = []
        self.addListSurface()
        self.surface = self.list_surface[self.index_surface]
        self.rect = self.surface.get_rect(topleft=(140, self.screen.height / 2))
        self.movement = 0
        # màn hình start game
        self.sf_title_game = Utilitie.surfaceScale('image/title.png', 14)
        self.rbird_start = self.surface.get_rect(midleft=(370, 180))

    def updateGameStart(self):
        rect_title = self.sf_title_game.get_rect(midleft=(70, 180))
        self.screen.window.blit(self.sf_title_game, rect_title)
        self.screen.window.blit(self.surface, self.rbird_start)

    def animation(self):
        self.surface = self.list_surface[self.index_surface]

    def addListSurface(self):
        for i in range(17):
            temp = image.load('image/bird/' + str(i) + '.jpg')
            w, h = Surface.get_size(temp)
            temp = transform.scale(temp, (w / 17, h / 17))
            self.list_surface.append(temp)

    @property
    def getY(self):
        return self.rect.y

    def handleJump(self):
        self.movement = -Bird.SPEED

    def resetGame(self):
        self.rect = self.surface.get_rect(center=(Bird.X, self.screen.height // 2))
        self.movement = 0

    def isCollision(self, rCols):  # return về True nếu con chim đã va chạm
        if self.rect.y <= 0 or self.rect.y >= self.screen.height - Floor.height:
            return True
        for rCol in rCols:
            if self.rect.colliderect(rCol["bottom"]) or self.rect.colliderect(rCol["top"]):
                return True
        return False

    def updateHandleGame(self):
        self.movement += Bird.GRAVITY
        self.rect.centery += self.movement
        self.screen.window.blit(self.surface, self.rect)

    def eventFly(self, event):
        if event.type == Bird.eventBirdFly:
            if self.index_surface < 16:
                self.index_surface += 1
            else:
                self.index_surface = 0
            self.animation()
