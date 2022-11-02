from pygame import image, transform, Rect
import pygame_gui





class StaticView:

    def __init__(self, screen, path='image/background/bg-2.jpg'):
        self.screen = screen
        self.sf_bg = transform.scale(image.load(path), (1920, self.screen.height))

        # view phần start gam
        self.sf_bg_start = image.load('image/background/bg-start.jpg')
        self.sf_bg_start = transform.scale(self.sf_bg_start, (1920, self.screen.height))

        size_btn = (200, 80)
        cordinate_btn = (self.screen.width // 2 - size_btn[0] / 2, 500)

        size_input = (260, 60)
        cordinate_input = (self.screen.width // 2 - size_input[0] / 2, 400)

        self.start_btn = pygame_gui.elements.UIButton(relative_rect=Rect(cordinate_btn, size_btn),
                                                      text='Start game',
                                                      manager=self.screen.manager)

        self.input_name = pygame_gui.elements.UITextEntryLine(relative_rect=Rect(cordinate_input,size_input),
                                                              manager=self.screen.manager,
                                                              object_id='#input-name')

        # khởi tạo button tai day.

    def draw_start_game(self):
        self.screen.window.blit(self.sf_bg_start, (0, 0))

    def draw_handle_game(self):
        self.screen.window.blit(self.sf_bg, (0, 0))
