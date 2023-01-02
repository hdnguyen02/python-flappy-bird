from pygame import image, transform
from random import randrange


class Pipe:
    WIDTH, HEIGHT = 60, 360
    SF_COL_BOTTOM = transform.scale(image.load('image/pipe/pipe.jpg'), (WIDTH, HEIGHT))
    SF_COL_TOP = transform.flip(SF_COL_BOTTOM, False, True)
    BLANK = 160
    DISTANCE = 200
    SPEED = 2

    def __init__(self, screen):
        self.cols = []
        self.screen = screen
        self.setup_col()

    def setup_col(self):
        for i in range(3):
            x = self.screen.width + i * self.DISTANCE
            y = randrange(-Pipe.HEIGHT + 120, 0, 20)
            self.cols.append([x, y])

    def draw_cols(self):
        for i in range(3):
            self.screen.draw_window(Pipe.SF_COL_TOP, (self.cols[i][0], self.cols[i][1]))
            self.screen.draw_window(Pipe.SF_COL_BOTTOM, (self.cols[i][0], self.cols[i][1] + self.BLANK + self.HEIGHT))

    def update_custom(self):
        self.draw_cols()
        for i in range(3):
            self.cols[i][0] -= Pipe.SPEED
        if self.cols[0][0] < -self.WIDTH:
            self.cols.pop(0)
            x = self.cols[1][0] + Pipe.DISTANCE
            y = randrange(-Pipe.HEIGHT + 120, 0, 20)
            self.cols.append([x, y])

    def reset_game(self):
        self.cols.clear()
