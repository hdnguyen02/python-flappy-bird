import sys
from pygame import event, QUIT, quit, KEYDOWN, K_SPACE, MOUSEBUTTONDOWN, display, image
from pygame import transform, font, mixer, mouse, time
from StaticView import StaticView
from Achievement import Achievement
from Floor import Floor
from Bird import Bird
from Pipe import Pipe
from Screen import Screen
from Utilitie import Button, Input, Utilitie


class Control:
    fps = 60
    bg_music = mixer.Sound('sound/flo.mp3')
    MOUSE_LEFT = 1

    def __init__(self):
        # Control.bg_music.play(loops=-1)
        self.screen = Screen((500, 700))

        self.floor = Floor(self.screen)
        self.static_view = StaticView(self.screen)
        self.bird = Bird(self.screen)
        self.pipe = Pipe(self.screen)
        self.achievement = Achievement(self.screen)

        self.is_sound = True
        self.is_play = True

        self.clock = time.Clock()

        # thử nghiệm với input
        computed_x_input = self.screen.width / 2 - 300 / 2
        self.input_name = Input(self.screen, computed_x_input, 415, 300, "Your name...", (0, 0, 128), 4)

    def update_view_play(self):
        self.static_view.draw_handle_game()
        self.bird.draw_handle_game(self.is_play)
        self.pipe.draw_handle_game(self.is_play)
        self.floor.draw_handle_game(self.is_play)
        self.achievement.draw_handle_game(self.is_play)
        display.update()

    def update_view_start(self):
        self.static_view.draw_start_game()
        self.floor.draw_handle_game(True)
        self.achievement.draw_start_game()
        self.bird.draw_game_start()

        self.input_name.draw()
        display.update()

    def show_rank(self):
        top_5 = self.achievement.top_5_user
        while True:
            self.clock.tick(Control.fps)
            for sub in event.get():
                Control.check_exit_game(sub)
                if sub.type == MOUSEBUTTONDOWN and sub.button == Control.MOUSE_LEFT:
                    pos = mouse.get_pos()
                    if self.static_view.btn_back.check_is_click(pos):
                        self.start_game()
            self.static_view.draw_rank(top_5)
            self.floor.draw_handle_game(True)
            display.update()

    @staticmethod
    def check_exit_game(sub_event):
        if sub_event.type == QUIT:
            quit()
            sys.exit()

    def start_game(self):
        while True:
            self.clock.tick(Control.fps)
            for sub in event.get():
                Control.check_exit_game(sub)
                self.bird.event_fly(sub)

                if sub.type == MOUSEBUTTONDOWN and sub.button == Control.MOUSE_LEFT:
                    pos = mouse.get_pos()

                    self.input_name.check_is_click(pos)
                    # check click start game
                    if self.static_view.btn_start.check_is_click(pos):
                        name = self.input_name.text
                        self.achievement.handle_sign_in(name)
                        self.handle_game()

                    # check click mute
                    if self.static_view.btn_sound.check_is_click(pos):
                        if self.is_sound:
                            mixer.pause()
                            self.static_view.btn_sound.change_sf(self.static_view.sf_btn_mute)
                        else:
                            mixer.unpause()
                            self.static_view.btn_sound.change_sf(self.static_view.sf_btn_sound)
                        self.is_sound = not self.is_sound

                    # check click bxh
                    if self.static_view.btn_rank.check_is_click(pos):
                        self.show_rank()

                self.input_name.handle_event(sub)
            self.update_view_start()

    def finish_game(self):
        w_screen = self.screen.width
        sf_game_over = Utilitie.surface_scale('image/gameOver.png', 6)
        centerx_game_over = self.screen.x_center(sf_game_over)

        # load vao table
        sf_table = Utilitie.surface_scale('image/tableScore1.png', 1.2)
        centerx_table = self.screen.x_center(sf_table)

        start_y_table = 700  # bằng
        end_y_table = 170

        str_score = str(self.achievement.score)
        sf_score = Utilitie.surface_font('font/font-result.ttf', 32, str_score, (0, 0, 0))
        sf_title_score = Utilitie.surface_font('font/font-result.ttf', 32, "- SCORE -", (0, 0, 0))

        str_best = str(self.achievement.top_5_user[0]["core"])
        sf_best = Utilitie.surface_font('font/font-result.ttf', 32, str_best, (0, 0, 0))
        sf_title_best = Utilitie.surface_font('font/font-result.ttf', 32, '< BEST > ', (0, 0, 0))

        # tính toán làm sao cho nó nhảy ra ở giữa.
        centerx_score = self.screen.x_center(sf_score)
        centerx_title_score = self.screen.x_center(sf_title_score)

        centerx_best = self.screen.x_center(sf_best)
        centerx_title_best = self.screen.x_center(sf_title_best)

        # tính toán điểm dừng chân của 4 thằng
        x_start_title_score = 0

        x_start_best = 500  # bằng với độ dài màn hình
        x_start_title_best = 500

        start_x_score = 0

        speed = 6
        y_start_game_over = 0
        y_end_game_over = 100

        #  khai bao nut tai cho nay.
        while True:
            self.clock.tick(60)
            for sub in event.get():
                Control.check_exit_game(sub)
                if sub.type == MOUSEBUTTONDOWN and sub.button == Control.MOUSE_LEFT:
                    pos = mouse.get_pos()
                    if self.static_view.btn_replay.check_is_click(pos):
                        self.bird.reset_game()
                        self.pipe.reset_game()
                        self.achievement.reset_game()
                        self.handle_game()

            # update hinh anh tai day.
            self.screen.window.blit(self.static_view.sf_bg_start, (0, 0))
            if y_start_game_over >= y_end_game_over:
                self.screen.window.blit(sf_game_over, (centerx_game_over, y_end_game_over))
            else:
                self.screen.window.blit(sf_game_over, (centerx_game_over, y_start_game_over))
            y_start_game_over += speed

            if end_y_table <= start_y_table:
                self.screen.window.blit(sf_table, (centerx_table, start_y_table))
            else:
                self.screen.window.blit(sf_table, (centerx_table, end_y_table))
            start_y_table -= 20

            if start_x_score < centerx_score:
                self.screen.window.blit(sf_score, (start_x_score, 250))
                start_x_score += 10
            else:
                self.screen.window.blit(sf_score, (centerx_score, 250))

            # vẽ ra title
            if x_start_title_score < centerx_title_score:
                self.screen.window.blit(sf_title_score, (start_x_score, 210))
                x_start_title_score += 10
            else:
                self.screen.window.blit(sf_title_score, (centerx_title_score, 210))

            # vẽ điểm best
            if x_start_best > centerx_best:
                self.screen.window.blit(sf_best, (x_start_best, 350))
                x_start_best -= 10
            else:
                self.screen.window.blit(sf_best, (centerx_best, 350))

            if x_start_title_best > centerx_title_best:
                self.screen.window.blit(sf_title_best, (x_start_title_best, 290))
                x_start_title_best -= 10
            else:
                self.screen.window.blit(sf_title_best, (centerx_title_best, 290))

            self.static_view.btn_replay.draw()
            self.floor.draw_handle_game(True)

            display.update()

    def handle_game(self):
        while True:
            self.clock.tick(Control.fps)
            for sub in event.get():
                Control.check_exit_game(sub)

                self.bird.event_fly(sub)

                is_space = sub.type == KEYDOWN and sub.key == K_SPACE
                is_mouse_left = sub.type == MOUSEBUTTONDOWN and sub.button == Control.MOUSE_LEFT

                if (is_space or is_mouse_left) and self.is_play:  # khi game còn chơi.
                    if self.is_sound:
                        self.bird.sound_space_click.play()
                    self.bird.handle_click_and_mouse()

                self.pipe.handle_create_pipe(sub)
            self.achievement.computed_score(self.pipe, self.bird, self.is_sound)

            self.update_view_play()
            self.is_play = not self.bird.is_collision(self.pipe)
            if not self.is_play:
                # khắc họa hình ảnh con chim chết
                self.achievement.handle_die()
                if self.is_sound:
                    Bird.sound_collision.play()
                    Bird.sound_die.play()
                self.finish_game()
