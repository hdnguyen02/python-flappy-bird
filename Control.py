from pygame import time, event, QUIT, quit, KEYDOWN, K_SPACE, MOUSEBUTTONDOWN
from View import View
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

    # getter
    @property
    def is_play(self):
        return self.__is_play

    def play_game(self):
        while self.__run:
            self.clock.tick(Control.__fps)
            for sub in event.get():
                if sub.type == QUIT:
                    self.__run = False

                is_space = sub.type == KEYDOWN and sub.key == K_SPACE
                is_mouse_left = sub.type == MOUSEBUTTONDOWN and sub.button == 1

                if is_space or is_mouse_left and self.is_play:  # khi game còn chơi.
                    self.bird.handle_click_and_mouse()
                elif is_space or is_mouse_left and not self.is_play:
                    self.__is_play = True
                    self.bird.reset_game()
                    self.pipe.reset_game()
                self.pipe.handle_create_pipe(sub)  # tạo ra các pipe

            self.view.update( self.__is_play, self.pipe, self.floor, self.bird)
            self.__is_play =  not self.bird.is_collision(self.pipe)

        quit()

    # xem lại code phần rect của floor
