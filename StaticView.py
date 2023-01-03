from Utilitie import Utilitie, Button


class StaticView:

    def __init__(self, screen):
        self.screen = screen
        self.sBackground = Utilitie.surfaceSize("image/background.jpg", (1920, self.screen.height))

        # btn - start
        sStartGame = Utilitie.surfaceScale('image/btn-start.jpg', 4)
        self.btnStartGame = Button(self.screen.width / 2, 540, sStartGame, self.screen)

        # btn - rank
        sRankStartGame = Utilitie.surfaceSize('image/rank.png', (90, 80))
        self.btnRankStartGame = Button(420, 60, sRankStartGame, self.screen)

        # sound and mute sound
        self.sSound = Utilitie.surfaceScale('image/musicOn.png', 6)
        self.sSoundMute = Utilitie.surfaceScale('image/musicOff.png', 6)
        self.btnSound = Button(80, 46, self.sSound, self.screen)

        # btn back
        sBack = Utilitie.surfaceScale('image/btn-back.png', 2)
        self.btnBack = Button(120, 70, sBack, self.screen)

        # laod vào cái table
        self.sTableRank = Utilitie.surfaceSize('image/tableScore1.png', (420, 400))
        self.sTops = [Utilitie.surfaceScale('image/top/Rank_' + str(path + 1) + '.png', 6) for path in range(5)]

        # btn replay finish
        sReplay = Utilitie.surfaceScale('image/btnReplay.png', 5)
        self.btnReplayFinish = Button(self.screen.width / 2 + 60, 480, sReplay, self.screen)

        # btn home finish
        sHomeFinish = Utilitie.surfaceScale('image/btnHome.png', 5)
        self.btnHomefinish = Button(self.screen.width / 2 - 60, 480, sHomeFinish, self.screen)

    def updateFinish(self):
        self.btnReplayFinish.draw()
        self.btnHomefinish.draw()

    def updateRank(self, top_user):
        self.screen.draw(self.sBackground, (0, 0))
        self.screen.draw(self.sTableRank, (40, 80 + 60 + 5))
        self.btnBack.draw()
        dis = 60
        for index, sf_top in enumerate(self.sTops):
            self.screen.draw(sf_top, (86, 195 + dis * index))

        # lấy ra sureface
        for index, user in enumerate(top_user):
            # lấy ra surface.
            info_user = user["name"] + "-" + str(user["core"])
            sf_user = Utilitie.surfaceFont('font/font-nomal.ttf', 26, info_user, (0, 0, 0))
            self.screen.draw(sf_user, (150, 205 + index * dis))

    def drawStartGame(self):
        self.screen.draw(self.sBackground, (0, 0))
        self.btnStartGame.draw()
        self.btnRankStartGame.draw()
        self.btnSound.draw()

    def updateHandleGame(self):
        self.screen.window.blit(self.sBackground, (0, 0))
