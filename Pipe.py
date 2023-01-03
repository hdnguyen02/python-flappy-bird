from pygame import image, transform
from random import randrange


class Pipe:
    WIDTH, HEIGHT = 60, 360
    SF_COL_BOTTOM = transform.scale(image.load('image/pipe.jpg'), (WIDTH, HEIGHT))
    SF_COL_TOP = transform.flip(SF_COL_BOTTOM, False, True)
    BLANK = 160
    DISTANCE = 220
    SPEED = 2

    def __init__(self, screen):
        self.__rCols = []
        self.screen = screen
        self.yPrevious = None

        # khởi tạo cột
        self.setupCols()

    def setupCols(self):
        for i in range(3):
            x = self.screen.width + i * self.DISTANCE
            y = self.__randomYCol()
            self.__rCols.append(Pipe.createRectCol(x, y))


    @property
    def getRCols(self):
        return self.__rCols

    @staticmethod
    def createRectCol(x, y):
        return {
            "pass": False,
            "top": Pipe.SF_COL_BOTTOM.get_rect(topleft=(x, y)),
            "bottom": Pipe.SF_COL_TOP.get_rect(topleft=(x, y + Pipe.BLANK + Pipe.HEIGHT))
        }

    def __randomYCol(self):
        while True:
            y = randrange(-Pipe.HEIGHT + 120, 0, 20)
            if y != self.yPrevious:
                return y

    def draw_cols(self):
        for rCol in self.__rCols:
            self.screen.draw(Pipe.SF_COL_TOP, rCol["top"])
            self.screen.draw(Pipe.SF_COL_BOTTOM, rCol["bottom"])

    def updateHandleGame(self, isPlay):
        self.draw_cols()
        if not isPlay:
            return
        for rCol in self.__rCols:
            rCol["top"].x -= Pipe.SPEED
            rCol["bottom"].x -= Pipe.SPEED
        if len(self.__rCols) != 0 and self.__rCols[0]["top"].x < -Pipe.WIDTH:
            self.__rCols.pop(0)
            x = self.__rCols[1]["top"].x + Pipe.DISTANCE
            y = self.__randomYCol()
            self.__rCols.append(Pipe.createRectCol(x, y))

    def resetGame(self):
        self.__rCols.clear()
        self.setupCols()
