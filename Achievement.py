from pygame import mixer, init, font
from Utilitie import Utilitie

init()

class Achievement:
    sound_pass = mixer.Sound('sound/congdiem.mp3')
    font_show_user = font.Font('font/show-user.ttf', 36)

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.name = None  # kiem tra neu nguoi dung khong nhap ten -> thi cho choi nhung khong xep hang.
        self.top_5_user = []
        self.read_file_top()

    def handle_sign_in(self, name):
        if name.strip() != '':
            self.name = name.strip()  # gán tên cho thằng này.

    @staticmethod
    def my_compare(user):
        return user["core"]

    def handle_die(self):
        if self.name and self.score >= self.top_5_user[4]["core"]:
            self.top_5_user.append(dict(name=self.name, core=self.score))
            self.top_5_user.sort(key=Achievement.my_compare, reverse=True)
            self.top_5_user.pop(len(self.top_5_user) - 1)
            self.ghi_file()

    def draw_start_game(self):
        str_show = 'top 1: ' + self.top_5_user[0]["name"] + "-" + str(self.top_5_user[0]["core"])
        sf_show_top = Utilitie.surface_font('font/font-nomal.ttf', 38, str_show, (29, 82, 32))
        rect_sf_high_user = sf_show_top.get_rect(center=(self.screen.width // 2, 300))
        self.screen.window.blit(sf_show_top, rect_sf_high_user)

    def write_file(self):
        pass

    def computed_score(self, rCols, xBird, is_sound):  # truyền vào đối tượng chim và đối tượng bird
        for rCol in rCols:
            if rCol["bottom"].right < xBird and not rCol["pass"]:
                if is_sound:
                    Achievement.sound_pass.play()
                self.score += 1
                rCol["pass"] = True

    def updateHandleGame(self, is_play):
        if not is_play:
            return
        margin_left = 26

        surface_score = Utilitie.surface_font('font/font-nomal.ttf', 32, str(self.score), (0, 0, 0))
        if self.name is not None:
            sf_user = Utilitie.surface_font('font/font-nomal.ttf', 32, self.name + ' -', (0, 0, 0))
            self.screen.window.blit(sf_user, (margin_left, 26))
            self.screen.window.blit(surface_score, (margin_left + sf_user.get_width() + 6, 26))
        else:
            self.screen.window.blit(surface_score, (margin_left + 6, 26))

    def reset_game(self):
        self.score = 0

    def read_file_top(self):
        file_top = open('top.txt', 'r')
        for line in file_top:
            name, score = line.rstrip().split('-')
            score = int(score)
            self.top_5_user.append(dict(name=name, core=score))
        file_top.close()

    # viet 1 ham ghi lai file
    def ghi_file(self):
        file = open('top.txt', 'w')
        temp = []
        for x in self.top_5_user:
            t = x['name'] + '-' + str(x['core']) + '\n'
            temp.append(t)
        file.writelines(temp)
        file.close()
