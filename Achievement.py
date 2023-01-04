from pygame import mixer, init, font
from Utilitie import Utilitie

init()


class Achievement:
    soundPass = mixer.Sound('sound/congdiem.mp3')
    font_show_user = font.Font('font/show-user.ttf', 36)

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.name = None  # kiem tra neu nguoi dung khong nhap ten -> thi cho choi nhung khong xep hang.
        self.top_5_user = []
        self.readFileTop()

    def handleSignIn(self, name):
        if name.strip() != '':
            self.name = name.strip()  # gán tên cho thằng này.

    @staticmethod
    def myCompare(user):
        return user["core"]

    def handleDie(self):
        if self.name and self.score > self.top_5_user[4]["core"]:
            self.top_5_user.append(dict(name=self.name, core=self.score))
            self.top_5_user.sort(key=Achievement.myCompare, reverse=True)
            self.top_5_user.pop(len(self.top_5_user) - 1)
            self.writeFileTop()

    def updateStartgame(self):
        str_show = 'top 1: ' + self.top_5_user[0]["name"] + "-" + str(self.top_5_user[0]["core"])
        sf_show_top = Utilitie.surfaceFont('font/font-nomal.ttf', 38, str_show, (29, 82, 32))
        rect_sf_high_user = sf_show_top.get_rect(center=(self.screen.width // 2, 300))
        self.screen.draw(sf_show_top, rect_sf_high_user)

    def computedScore(self, rCols, xBird, isSound):  # truyền vào đối tượng chim và đối tượng bird
        for rCol in rCols:
            if rCol["bottom"].right < xBird and not rCol["pass"]:
                if isSound:
                    Achievement.soundPass.play()
                self.score += 1
                rCol["pass"] = True

    def updateHandleGame(self, is_play):
        if not is_play:
            return
        margin_left = 26

        surface_score = Utilitie.surfaceFont('font/font-nomal.ttf', 40, str(self.score), (0, 0, 0))
        if self.name is not None:
            sf_user = Utilitie.surfaceFont('font/font-nomal.ttf', 40, self.name + ' -', (0, 0, 0))
            self.screen.window.blit(sf_user, (margin_left, 26))
            self.screen.window.blit(surface_score, (margin_left + sf_user.get_width() + 6, 26))
        else:
            self.screen.window.blit(surface_score, (margin_left + 6, 26))

    def resetGame(self):
        self.score = 0

    def readFileTop(self):
        file_top = open('top.txt', 'r')
        for line in file_top:
            name, score = line.rstrip().split('-')
            score = int(score)
            self.top_5_user.append(dict(name=name, core=score))
        file_top.close()

    # viet 1 ham ghi lai file
    def writeFileTop(self):
        file = open('top.txt', 'w')  # w : file được làm trống trươc khi được thêm vào
        temp = []
        for x in self.top_5_user:
            t = x['name'] + '-' + str(x['core']) + '\n'
            temp.append(t)
        file.writelines(temp)
        file.close()
