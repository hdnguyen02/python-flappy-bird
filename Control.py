import sys

from pygame import event, QUIT, quit, KEYDOWN, K_SPACE, MOUSEBUTTONDOWN, display, font, mixer, mouse, image
from pygame import transform
import time
from StaticView import StaticView
from Achievement import Achievement
from Floor import Floor
from Bird import Bird
from Pipe import Pipe
from Screen import Screen
import pygame_gui
import pygame
from Button import Button


class Control:
    __fps = 60
    #   khai báo font.
    font_game = font.Font('font/TypefaceMario64-ywA93.otf', 40)

    # tạo ra âm thanh siêng xuốt trò chơi
    bg_music = mixer.Sound('sound/flo.mp3')
    bg_music.play(loops=-1)

    # load nhạc vào cho game

    def __init__(self):
        self.size_screen = (500, 700)
        self.screen = Screen(self.size_screen)

        self.floor = Floor(self.screen)
        self.static_view = StaticView(self.screen)
        self.bird = Bird(self.screen)
        self.pipe = Pipe(self.screen)
        self.achievement = Achievement(self.screen)
        self.is_start = True
        self.is_sound = True  # cho phep am thanh.

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

    def show_rank(self):
        # Tao ra nut quay lai.
        # tao ra nut home
        sf_home = image.load('image/home.png')
        w_home, h_home = sf_home.get_size()
        sf_home = transform.scale(sf_home, (w_home / 7, h_home / 7))
        btn_home = Button(60, 60, sf_home, self.screen)

        # lay ra 5 cai nut xep hang

        sf_top1 = image.load('image/top/Rank_1.png')

        sf_top2 = image.load('image/top/Rank_2.png')
        sf_top3 = image.load('image/top/Rank_3.png')
        sf_top4 = image.load('image/top/Rank_4.png')
        sf_top5 = image.load('image/top/Rank_5.png')

        w_top, h_top = sf_top1.get_size()
        sf_top1 = transform.scale(sf_top1, (w_top / 4, h_top / 4))
        sf_top2 = transform.scale(sf_top2, (w_top / 4, h_top / 4))
        sf_top3 = transform.scale(sf_top3, (w_top / 4, h_top / 4))
        sf_top4 = transform.scale(sf_top4, (w_top / 4, h_top / 4))
        sf_top5 = transform.scale(sf_top5, (w_top / 4, h_top / 4))

        while True:
            self.clock.tick(Control.__fps)
            for sub in event.get():
                if sub.type == QUIT:
                    quit()
                    sys.exit()
                if sub.type == MOUSEBUTTONDOWN and sub.button == 1:
                    pos = mouse.get_pos()
                    if btn_home.check_is_click(pos):
                        self.start_game()

            # ve nut quay lai.
            # lay ra danh sach top 5 tai day.
            top_5 = self.achievement.top_5_user  # sau khi lay ra + get_font.
            font_show = font.Font('font/TypefaceMario64-ywA93.otf', 26)

            # tao ra 5 sf user
            sf_top5_user = []

            for user in top_5:
                temp_sf = font_show.render(user["name"] + " - " + str(user["core"]), True, (0, 0, 0))
                sf_top5_user.append(temp_sf)

            distance = 85
            self.screen.window.blit(self.static_view.sf_bg_start, (0, 0))
            btn_home.draw()
            self.screen.window.blit(sf_top1, (26, 120))
            self.screen.window.blit(sf_top2, (26, 120 + distance))
            self.screen.window.blit(sf_top3, (26, 120 + distance * 2))
            self.screen.window.blit(sf_top4, (26, 120 + distance * 3))
            self.screen.window.blit(sf_top5, (26, 120 + distance * 4))

            # ve len tren man hinh
            index = 0
            for sf in sf_top5_user:
                self.screen.window.blit(sf, (100, 140 + index * distance))
                index += 1

            display.update()

    def start_game(self):

        while True:
            time_delta = self.clock.tick(Control.__fps) / 1000
            for sub in event.get():
                if sub.type == QUIT:
                    quit()
                    sys.exit()
                # press start game
                if sub.type == MOUSEBUTTONDOWN and sub.button == 1:
                    pos = mouse.get_pos()
                    # start game
                    if self.static_view.btn_start.check_is_click(pos):
                        name = self.static_view.input_name.get_text()
                        print('name',name)
                        self.achievement.handle_sign_in(name)
                        self.handle_game()

                    # mute.
                    if self.static_view.btn_sound.check_is_click(pos):
                        if self.is_sound:
                            mixer.pause()
                            self.static_view.btn_sound.change_sf(self.static_view.sf_btn_mute)
                        else:
                            mixer.unpause()
                            self.static_view.btn_sound.change_sf(self.static_view.sf_btn_sound)
                        self.is_sound = not self.is_sound

                    # bxh
                    if self.static_view.btn_rank.check_is_click(pos):
                        self.show_rank()

                if sub.type == Bird.bird_fly:
                    if self.bird.index_surface < 16:
                        self.bird.index_surface += 1
                    else:
                        self.bird.index_surface = 0
                    self.bird.animation()

                self.screen.manager.process_events(sub)

            self.static_view.draw_start_game()
            self.achievement.draw_start_game()
            self.floor.draw_handle_game(True)
            self.bird.draw_game_start()

            self.screen.manager.update(time_delta)

            self.screen.manager.draw_ui(self.screen.window)

            display.update()

    def finish_game(self):

        # game over
        w_screen = self.screen.width
        sf_game_over = image.load('image/gameOver.png')
        w_over, h_over = sf_game_over.get_size()
        sf_game_over = transform.scale(sf_game_over, (w_over / 6, h_over / 6))
        w_over, h_over = sf_game_over.get_size()

        # load button
        sf_replay_btn = image.load('image/replay2.png')
        w_replay, h_replay = sf_replay_btn.get_size()
        sf_replay_btn = transform.scale(sf_replay_btn, (w_replay / 2.5, h_replay / 2.5))

        rect_replay = sf_replay_btn.get_rect(center=(w_screen / 2, 480))

        btn_replay = Button(w_screen / 2,480,sf_replay_btn,self.screen)

        # load vao table
        sf_table_show = image.load('image/tableScore1.png')
        w_table, h_table = sf_table_show.get_size()
        sf_table_show = transform.scale(sf_table_show, (w_table / 1.2, h_table / 1.2))
        w_table, h_table = sf_table_show.get_size()
        # tính toán tọa đô x
        x_center_table = w_screen / 2 - w_table / 2
        start_y_table = 700  # bằng
        end_y_table = 170

        # lua chon font
        font_show = font.Font('font/show-user.ttf', 36)



        # tạo ra tiêu đề
        title_score = "- SCORE -"
        str_score = str(self.achievement.score)
        sf_title_score = font_show.render(title_score,True,(0, 0, 0))
        sf_score = font_show.render(str_score, True, (0, 0, 0))

        # tính toán làm sao cho nó nhảy ra ở giữa.
        center_x_score =  w_screen / 2 - sf_score.get_width() / 2
        center_x_title_score = w_screen / 2 - sf_title_score.get_width() / 2

        title_best = "< BEST >"
        str_best = str(self.achievement.top_5_user[0]["core"])
        sf_best = font_show.render(str_best, True, (0, 0, 0))
        sf_title_best = font_show.render(title_best, True, (0, 0, 0))

        center_x_best = w_screen / 2 - sf_best.get_width() / 2
        center_x_title_best = w_screen / 2 - sf_title_best.get_width() / 2

        # tính toán điểm dừng chân của 4 thằng
        x_start_title_score = 0

        x_start_best = 500 # bằng với độ dài màn hình
        x_start_title_best = 500


        start_x_high = 500
        end_y_high = 250



        start_x_score = 0


        speed = 6
        y_start_game_over = 0
        y_end_game_over = 100

        #  khai bao nut tai cho nay.
        while True:
            self.clock.tick(60)
            for sub in event.get():
                if sub.type == QUIT:
                    quit()
                    sys.exit()
                if sub.type == MOUSEBUTTONDOWN and sub.button == 1:
                    pos = mouse.get_pos()
                    if btn_replay.check_is_click(pos):
                        self.bird.reset_game()
                        self.pipe.reset_game()
                        self.achievement.reset_game()
                        self.handle_game()

            # update hinh anh tai day.
            self.screen.window.blit(self.static_view.sf_bg_start, (0, 0))
            if (y_start_game_over >= y_end_game_over):
                self.screen.window.blit(sf_game_over, (w_screen / 2 - w_over / 2, y_end_game_over))
            else:
                self.screen.window.blit(sf_game_over, (w_screen / 2 - w_over / 2, y_start_game_over))
            y_start_game_over += speed

            if (end_y_table <= start_y_table):
                self.screen.window.blit(sf_table_show, (x_center_table, start_y_table))
            else:
                self.screen.window.blit(sf_table_show, (x_center_table, end_y_table))
            start_y_table -= 20

            if start_x_score < center_x_score:
                self.screen.window.blit(sf_score, (start_x_score, 250))
                start_x_score += 10
            else:
                self.screen.window.blit(sf_score, (center_x_score, 250))

            # vẽ ra title
            if x_start_title_score < center_x_title_score:
                self.screen.window.blit(sf_title_score, (start_x_score, 210))
                x_start_title_score+=10
            else:
                self.screen.window.blit(sf_title_score, (center_x_title_score, 210))

            # vẽ điểm best
            if x_start_best > center_x_best:
                self.screen.window.blit(sf_best,(x_start_best,350))
                x_start_best -= 10
            else:
                self.screen.window.blit(sf_best,(center_x_best,350))

            if x_start_title_best > center_x_title_best:
                self.screen.window.blit(sf_title_best,(x_start_title_best,290))
                x_start_title_best -= 10
            else:
                self.screen.window.blit(sf_title_best,(center_x_title_best,290))


            btn_replay.draw()

            display.update()

    def handle_game(self):
        while True:
            self.clock.tick(Control.__fps)
            for sub in event.get():
                if sub.type == QUIT:
                    quit()
                    sys.exit()

                is_space = sub.type == KEYDOWN and sub.key == K_SPACE
                is_mouse_left = sub.type == MOUSEBUTTONDOWN and sub.button == 1

                if (is_space or is_mouse_left) and self.is_play:  # khi game còn chơi.
                    if self.is_sound:
                        self.bird.sound_space_click.play()
                    self.bird.handle_click_and_mouse()
                # elif (is_space or is_mouse_left) and not self.is_play:
                #     self.finish_game()  # sử lý kết thúc game.

                if sub.type == Bird.bird_fly:
                    if self.bird.index_surface < 16:
                        self.bird.index_surface += 1
                    else:
                        self.bird.index_surface = 0
                    self.bird.animation()

                self.pipe.handle_create_pipe(sub)
            self.achievement.computed_score(self.pipe, self.bird, self.is_sound)

            self.control_view_hadle_game()
            self.is_play = not self.bird.is_collision(self.pipe)
            if not self.is_play:
                self.achievement.handle_die()
                if self.is_sound:
                    Bird.sound_collision.play()
                    Bird.sound_die.play()
                self.finish_game()
