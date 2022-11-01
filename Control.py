from pygame import time, event, QUIT, quit, KEYDOWN, K_SPACE, MOUSEBUTTONDOWN
from View import View, Achievement
from Floor import Floor
from Bird import Bird
from Pipe import Pipe



class Control:
    __fps = 60

    def __init__(self):
        self.clock = time.Clock()
        self.__run = True  # vẫn còn chơi game
        self.__is_play = True  # đang trong 1 ván game
        self.floor = Floor()
        self.view = View()
        self.bird = Bird()
        self.pipe = Pipe()
        self.achievement = Achievement()  # chứa thành tích của người chơi.
        self.temp = True

    # getter
    @property
    def is_play(self):
        return self.__is_play



    def play_game(self):
        self.handle_game()

    def finish_game(self):
        pass

    def handle_game(self):
        while self.__run:
            self.clock.tick(Control.__fps)
            for sub in event.get():
                if sub.type == QUIT:
                    self.__run = False

                is_space = sub.type == KEYDOWN and sub.key == K_SPACE
                is_mouse_left = sub.type == MOUSEBUTTONDOWN and sub.button == 1

                if (is_space or is_mouse_left) and self.is_play:  # khi game còn chơi.
                    self.bird.handle_click_and_mouse()
                elif (is_space or is_mouse_left) and not self.is_play:
                    self.finish_game()  # sử lý kết thúc game.

                if sub.type == Bird.bird_fly:
                    if self.bird.index_surface < 16:
                        self.bird.index_surface += 1
                    else:
                        self.bird.index_surface = 0
                    self.bird.animation()

                self.pipe.handle_create_pipe(sub)
            self.achievement.computed_score(self.pipe, self.bird)
            self.view.update(self.__is_play, self.pipe, self.floor, self.bird, self.achievement)
            self.__is_play = not self.bird.is_collision(self.pipe)
        quit()




