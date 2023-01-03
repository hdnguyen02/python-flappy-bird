from pygame import image, transform, font, draw, Rect, KEYDOWN, K_SPACE, K_BACKSPACE, K_RETURN

font.init()


class Utilitie:
    @staticmethod
    def surfaceSize(path, size):
        surface = transform.scale(image.load(path), size)
        return surface

    @staticmethod
    def surfaceScale(path, scale):
        surface = image.load(path)
        width, height = surface.get_size()
        # update witdh HEIGHT
        width = width / scale
        height = height / scale

        surface = transform.scale(surface, (width, height))
        return surface

    @staticmethod
    def surfaceFont(path_font, size_font, title, color):
        use_font = font.Font(path_font, size_font)
        surface = use_font.render(title, True, color)
        return surface


class Button:
    def __init__(self, x_center, y_center, surface, screen):
        self.screen = screen
        self.sf = surface
        self.rect = self.sf.get_rect(center=(x_center, y_center))

    def draw(self):
        self.screen.window.blit(self.sf, self.rect)

    def checkClick(self, pos):
        x_pos, y_pos = pos
        if x_pos in range(self.rect.left, self.rect.right) and y_pos in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeSF(self, newSF):
        self.sf = newSF


class Input:
    def __init__(self, screen, x, y, width, hint, color, border=1):
        self.screen = screen
        self.hint = hint
        self.x = x
        self.width = width
        self.y = y
        self.color = color
        self.border = border
        self.height = 40
        # tạo ra rect cho input
        self.rect = Rect((self.x, self.y - self.height), (self.width, self.height))
        self.select = False
        self.text = ''
        self.size = 26

    def draw(self):
        if not self.text:
            sf_text = Utilitie.surfaceFont('font/font-nomal.ttf', 26, self.hint, (0, 0, 0))
        else:
            sf_text = Utilitie.surfaceFont('font/font-nomal.ttf', 26, self.text, (0, 0, 0))

        self.screen.draw(sf_text, (self.x + 10, self.y - self.height / 2 - 10))
        draw.line(self.screen.window, self.color, (self.x, self.y), (self.x + self.width, self.y), self.border)

    def checkClick(self, pos):
        x_pos, y_pos = pos
        if x_pos in range(self.rect.left, self.rect.right) and y_pos in range(self.rect.top, self.rect.bottom):
            if not self.select:
                self.select = True
                self.text += '_'
        else:
            if self.select:
                self.select = False
                self.text = self.text[:-1]

    def handleEvent(self, event):
        if self.select and event.type == KEYDOWN:
            self.text = self.text[:-1]
            if event.key == K_SPACE:
                self.text += ' ' + '_'
            elif event.key == K_RETURN:
                self.select = False
            elif event.key == K_BACKSPACE:
                if len(self.text) == 1:
                    self.text = ''
                else:
                    self.text = self.text[:-1] + '_'

            elif event.unicode.isalpha():
                self.text += event.unicode + '_'