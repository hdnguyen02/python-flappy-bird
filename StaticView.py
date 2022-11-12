from Utilitie import Utilitie, Button


class StaticView:

    def __init__(self, screen, path='image/background/bg-2.jpg'):
        self.screen = screen
        self.sf_bg = Utilitie.surface_size(path, (1920, self.screen.height))

        path_bg_start = 'image/background/bg-3.jpg'
        self.sf_bg_start = Utilitie.surface_size(path_bg_start, (1920, self.screen.height))

        # btn - start
        sf_btn_start = Utilitie.surface_scale('image/button/btn-start.jpg', 4)
        self.btn_start = Button(self.screen.width / 2, 540, sf_btn_start, self.screen)

        # btn - rank
        sf_btn_rank = Utilitie.surface_size('image/rank.png', (90, 80))
        self.btn_rank = Button(420, 60, sf_btn_rank, self.screen)

        # sound and mute sound
        self.sf_btn_sound = Utilitie.surface_scale('image/musicOn.png', 6)
        self.sf_btn_mute = Utilitie.surface_scale('image/musicOff.png', 6)
        self.btn_sound = Button(80, 46, self.sf_btn_sound, self.screen)

        # btn back
        sf_back = Utilitie.surface_scale('image/btn-back.png', 2)
        self.btn_back = Button(120, 70, sf_back, self.screen)

        # laod vào cái table
        self.sf_table = Utilitie.surface_size('image/tableScore1.png', (420, 400))
        self.sf_tops = [Utilitie.surface_scale('image/top/Rank_' + str(path + 1) + '.png', 6) for path in range(5)]

        # btn replay
        sf_replay = Utilitie.surface_scale('image/replay2.png', 2.5)
        self.btn_replay = Button(self.screen.width / 2, 480, sf_replay, self.screen)

    def draw_rank(self, top_user):
        self.screen.draw_window(self.sf_bg_start, (0, 0))
        self.screen.draw_window(self.sf_table, (40, 80 + 60 + 5))
        self.btn_back.draw()
        dis = 60
        for index, sf_top in enumerate(self.sf_tops):
            self.screen.draw_window(sf_top, (86, 195 + dis * index))

        # lấy ra sureface
        for index, user in enumerate(top_user):
            # lấy ra surface.
            info_user = user["name"] + "-" + str(user["core"])
            sf_user = Utilitie.surface_font('font/font-nomal.ttf', 26, info_user, (0, 0, 0))
            self.screen.draw_window(sf_user, (150, 205 + index * dis))

    def draw_start_game(self):
        self.screen.draw_window(self.sf_bg_start, (0, 0))
        self.btn_start.draw()
        self.btn_rank.draw()
        self.btn_sound.draw()

    def draw_handle_game(self):
        self.screen.window.blit(self.sf_bg, (0, 0))
