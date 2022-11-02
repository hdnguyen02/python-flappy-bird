
from pygame import time, event, QUIT, quit, KEYDOWN, K_SPACE, MOUSEBUTTONDOWN,display, font

from Static_view import Static_view, Achievement
from Floor import Floor
from Bird import Bird
from Pipe import Pipe
from Screen import Screen




class Control:
    __fps = 60
    #   khai báo font.
    font_game = font.Font('font/TypefaceMario64-ywA93.otf',40)

    def __init__(self):
        self.size_screen = (500, 700)
        self.screen = Screen(self.size_screen)

        self.floor = Floor(self.screen)
        self.static_view = Static_view(self.screen)
        self.bird = Bird(self.screen)
        self.pipe = Pipe(self.screen)
        self.achievement = Achievement(self.screen,Control.font_game)


        self.clock = time.Clock()
        self.__run = True  # vẫn còn chơi game
        self.__is_play = True  # đang trong 1 ván game

    # getter
    @property
    def is_play(self):
        return self.__is_play

    def update_view(self):
        self.static_view.update_view()
        self.bird.draw(self.is_play)
        self.pipe.draw(self.is_play)
        self.floor.draw(self.is_play)
        self.achievement.draw(self.is_play)

        display.update()


    def play_game(self):
        self.handle_game()

    def start_game(self):
        pass

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


            #  update.
            self.update_view()
            self.__is_play = not self.bird.is_collision(self.pipe)
        quit()




