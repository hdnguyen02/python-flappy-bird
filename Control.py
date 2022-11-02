from pygame import event, QUIT, quit, KEYDOWN, K_SPACE, MOUSEBUTTONDOWN, display, font, mixer
import time
from StaticView import StaticView
from Achievement import Achievement
from Floor import Floor
from Bird import Bird
from Pipe import Pipe
from Screen import Screen
import pygame_gui
import pygame


class Control:
    __fps = 60
    #   khai báo font.
    font_game = font.Font('font/TypefaceMario64-ywA93.otf', 40)



    # load nhạc vào cho game


    def __init__(self):
        self.size_screen = (500, 700)
        self.screen = Screen(self.size_screen)

        self.floor = Floor(self.screen)
        self.static_view = StaticView(self.screen)
        self.bird = Bird(self.screen)
        self.pipe = Pipe(self.screen)
        self.achievement = Achievement(self.screen, Control.font_game)
        self.is_start = True

        self.clock = pygame.time.Clock()
        self.run = True  # vẫn còn chơi game
        self.is_play = True  # đang trong 1 ván game

    def control_view_hadle_game(self):
        self.static_view.draw_handle_game()
        self.bird.draw_handle_game(self.is_play)
        self.pipe.draw_handle_game(self.is_play)
        self.floor.draw_handle_game(self.is_play)
        self.achievement.draw_handle_game(self.is_play)
        display.update()

    def play_game(self):
        self.start_game()

    def start_game(self):

        while self.run:
            time_delta = self.clock.tick(Control.__fps) / 1000
            for sub in event.get():
                if sub.type == QUIT:
                    self.run = False # người dùng tắt game.

                if sub.type == pygame_gui.UI_BUTTON_PRESSED:
                    if sub.ui_element == self.static_view.start_btn:
                        self.handle_game()
                        return
                if sub.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and sub.ui_object_id == '#input-name':
                    print('hello word ahihi')  # chỗ này kiêm tra xem người dùng nhập tên chưa.

                self.screen.manager.process_events(sub)

            self.static_view.draw_start_game()

            self.screen.manager.update(time_delta)

            self.screen.manager.draw_ui(self.screen.window)

            display.update()

    def finish_game(self):
        pass

    def handle_game(self):
        while self.run:
            self.clock.tick(Control.__fps)
            for sub in event.get():
                if sub.type == QUIT:
                    self.run = False

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

            self.control_view_hadle_game()
            self.is_play = not self.bird.is_collision(self.pipe)
            if not self.is_play:

                Bird.sound_collision.play()
                Bird.sound_die.play()
                time.sleep(1)
                return
        quit()
