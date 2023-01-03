import sys
from pygame import event, QUIT, quit, KEYDOWN, K_SPACE, MOUSEBUTTONDOWN, display
from pygame import mixer, mouse, time
from StaticView import StaticView
from Achievement import Achievement
from Floor import Floor
from Bird import Bird
from Pipe import Pipe
from Screen import Screen
from Utilitie import Input, Utilitie


class Control:
    fps = 60
    bg_music = mixer.Sound('sound/nhacNen.mp3')
    MOUSE_LEFT = 1

    def __init__(self):
        # Control.bg_music.play(loops=-1)
        self.screen = Screen((500, 700))

        self.floor = Floor(self.screen)
        self.staticView = StaticView(self.screen)
        self.bird = Bird(self.screen)
        self.pipe = Pipe(self.screen)
        self.achievement = Achievement(self.screen)

        self.isSound = True
        self.ispLay = True

        self.clock = time.Clock()

        # input
        computed_x_input = self.screen.width / 2 - 300 / 2
        self.input_name = Input(self.screen, computed_x_input, 415, 300, "Your name...", (0, 0, 128), 4)

    def updateHandleGame(self):
        self.staticView.draw_handle_game()
        self.bird.draw_handle_game()
        self.pipe.updateHandleGame(self.ispLay)
        self.floor.draw_handle_game(self.ispLay)
        self.achievement.updateHandleGame(self.ispLay)
        display.update()

    def updateStart(self):
        self.staticView.drawStartGame()
        self.floor.draw_handle_game(True)
        self.achievement.updateStartgame()
        self.bird.draw_game_start()

        self.input_name.draw()
        display.update()

    def showRank(self):
        top_5 = self.achievement.top_5_user
        while True:
            self.clock.tick(Control.fps)
            for sub in event.get():
                Control.checkExitGame(sub)
                if sub.type == MOUSEBUTTONDOWN and sub.button == Control.MOUSE_LEFT:
                    pos = mouse.get_pos()
                    if self.staticView.btnBack.checkClick(pos):
                        self.startGame()
            self.staticView.updateRank(top_5)
            self.floor.draw_handle_game(True)
            display.update()

    @staticmethod
    def checkExitGame(subEvent):
        if subEvent.type == QUIT:
            quit()
            sys.exit()

    def startGame(self):
        while True:
            self.clock.tick(Control.fps)
            for sub in event.get():
                Control.checkExitGame(sub)
                self.bird.event_fly(sub)

                if sub.type == MOUSEBUTTONDOWN and sub.button == Control.MOUSE_LEFT:
                    pos = mouse.get_pos()

                    self.input_name.checkClick(pos)
                    # check click start game
                    if self.staticView.btnStartGame.checkClick(pos):
                        name = self.input_name.text
                        self.achievement.handleSignIn(name)
                        self.handlGame()

                    # check click mute
                    if self.staticView.btnSound.checkClick(pos):
                        if self.isSound:
                            mixer.pause()
                            self.staticView.btnSound.changeSF(self.staticView.sSoundMute)
                        else:
                            mixer.unpause()
                            self.staticView.btnSound.changeSF(self.staticView.sSound)
                        self.isSound = not self.isSound

                    # check click bxh
                    if self.staticView.btnRankStartGame.checkClick(pos):
                        self.showRank()

                self.input_name.handleEvent(sub)
            self.updateStart()

    def resetGame(self):
        self.bird.reset_game()
        self.pipe.reset_game()
        self.achievement.resetGame()
        self.ispLay = True

    def finishGame(self):
        sf_game_over = Utilitie.surfaceScale('image/gameOver.png', 6)
        centerx_game_over = self.screen.midleXScreen(sf_game_over)

        # load vao table
        sf_table = Utilitie.surfaceScale('image/tableScore1.png', 1.2)
        centerx_table = self.screen.midleXScreen(sf_table)

        start_y_table = 700
        end_y_table = 170

        str_score = str(self.achievement.score)
        sf_score = Utilitie.surfaceFont('font/fontScore.ttf', 40, str_score, (0, 0, 0))
        sf_title_score = Utilitie.surfaceFont('font/fontScore.ttf', 40, "- SCORE -", (0, 0, 0))

        str_best = str(self.achievement.top_5_user[0]["core"])
        sf_best = Utilitie.surfaceFont('font/fontScore.ttf', 40, str_best, (0, 0, 0))
        sf_title_best = Utilitie.surfaceFont('font/fontScore.ttf', 40, '< BEST > ', (0, 0, 0))

        # tính toán làm sao cho nó nhảy ra ở giữa.
        centerx_score = self.screen.midleXScreen(sf_score)
        centerx_title_score = self.screen.midleXScreen(sf_title_score)

        centerx_best = self.screen.midleXScreen(sf_best)
        centerx_title_best = self.screen.midleXScreen(sf_title_best)

        # tính toán điểm dừng chân của 4 thằng
        x_start_title_score = 0

        x_start_best = 500  # bằng với độ dài màn hình
        x_start_title_best = 500

        start_x_score = 0

        y_start_game_over = 0
        y_end_game_over = 100

        while True:
            self.clock.tick(60)
            for sub in event.get():
                Control.checkExitGame(sub)
                if sub.type == MOUSEBUTTONDOWN and sub.button == Control.MOUSE_LEFT:
                    pos = mouse.get_pos()
                    if self.staticView.btnReplayFinish.checkClick(pos):
                        self.resetGame()
                        self.handlGame()

                    elif self.staticView.btnHomefinish.checkClick(pos):
                        self.resetGame()
                        self.startGame()

            # update hinh anh tai day.
            self.screen.window.blit(self.staticView.sBackground, (0, 0))
            if y_start_game_over >= y_end_game_over:
                self.screen.window.blit(sf_game_over, (centerx_game_over, y_end_game_over))
            else:
                self.screen.window.blit(sf_game_over, (centerx_game_over, y_start_game_over))
            y_start_game_over += 20

            if end_y_table <= start_y_table:
                self.screen.window.blit(sf_table, (centerx_table, start_y_table))
            else:
                self.screen.window.blit(sf_table, (centerx_table, end_y_table))
            start_y_table -= 30

            if start_x_score < centerx_score:
                self.screen.window.blit(sf_score, (start_x_score, 250))
                start_x_score += 20
            else:
                self.screen.window.blit(sf_score, (centerx_score, 250))

            # vẽ ra title
            if x_start_title_score < centerx_title_score:
                self.screen.window.blit(sf_title_score, (start_x_score, 190))
                x_start_title_score += 20
            else:
                self.screen.window.blit(sf_title_score, (centerx_title_score, 200))

            # vẽ điểm best
            if x_start_best > centerx_best:
                self.screen.window.blit(sf_best, (x_start_best, 350))
                x_start_best -= 20
            else:
                self.screen.window.blit(sf_best, (centerx_best, 350))

            if x_start_title_best > centerx_title_best:
                self.screen.window.blit(sf_title_best, (x_start_title_best, 300))
                x_start_title_best -= 20
            else:
                self.screen.window.blit(sf_title_best, (centerx_title_best, 300))

            self.staticView.btnReplayFinish.draw()
            self.staticView.btnHomefinish.draw()
            self.floor.draw_handle_game(True)

            display.update()

    def handlGame(self):
        while True:
            if not self.ispLay:
                self.achievement.handleDie()
                if self.isSound:
                    Bird.sound_collision.play()
                    Bird.sound_die.play()
                # kiểm tra tại chỗ này
                while self.bird.getY <= self.screen.height:
                    self.clock.tick(Control.fps)
                    self.updateHandleGame()

                self.finishGame()

            self.clock.tick(Control.fps)
            for sub in event.get():
                Control.checkExitGame(sub)
                self.bird.event_fly(sub)
                is_space = sub.type == KEYDOWN and sub.key == K_SPACE
                is_mouse_left = sub.type == MOUSEBUTTONDOWN and sub.button == Control.MOUSE_LEFT

                if (is_space or is_mouse_left) and self.ispLay:  # khi game còn chơi.
                    if self.isSound:
                        self.bird.sound_space_click.play()
                    self.bird.handle_click_and_mouse()

            self.achievement.computedScore(self.pipe.getRCols, Bird.X, self.isSound)
            self.updateHandleGame()
            self.ispLay = not self.bird.isCcollision(self.pipe.getRCols)
