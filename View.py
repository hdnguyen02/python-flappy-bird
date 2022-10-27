from pygame import image, init, display, transform


class Screen:
    width = 500
    height = 700
    size = (width, height)
    window = display.set_mode(size)


class View(Screen):
    def __init__(self):
        init()
        self.bg = image.load('image/background/bg.png')
        self.bg = transform.scale(self.bg, (1920, Screen.height))
        display.set_caption('Flappy Bird')

    def update(self, is_play, *args):  # để có thể sử lấy ra các biến trong control.
        Screen.window.blit(self.bg, (0, 0))
        for sub in args:
            sub.draw(Screen.window, is_play)
        display.update()
