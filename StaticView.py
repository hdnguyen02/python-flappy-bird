from pygame import image, transform, Rect, font
import pygame_gui

from Button import Button

font.init()


class StaticView:
    font_title = font.Font('font/TypefaceMario64-ywA93.otf',26)


    def __init__(self, screen, path='image/background/bg-2.jpg'):
        self.screen = screen
        self.sf_bg = transform.scale(image.load(path), (1920, self.screen.height))

        # view phần start gam
        self.sf_bg_start = image.load('image/background/bg.jpg')
        self.sf_bg_start = transform.scale(self.sf_bg_start, (1920, self.screen.height))

        self.replay_btn = pygame_gui.elements.UIButton(relative_rect=Rect((0, 0), (200, 60)),
                                                  text='replay game',
                                                  manager=self.screen.manager_finish)

        # btn - start

        sf_btn_start = image.load('image/button/start-removebg-preview.jpg')
        sf_btn_start = transform.scale(sf_btn_start,(160,80))
        self.btn_start = Button(self.screen.width / 2,520,sf_btn_start,self.screen)

        # btn - rank
        sf_btn_rank = image.load('image/rank.png')
        sf_btn_rank = transform.scale(sf_btn_rank,(90,80))
        self.btn_rank = Button(420,60,sf_btn_rank,self.screen)

        # sound and mute sound
        self.sf_btn_sound = image.load('image/musicOn.png')
        w_btn_sound,h_btn_sound = self.sf_btn_sound.get_size()
        self.sf_btn_sound = transform.scale(self.sf_btn_sound,(w_btn_sound / 6,h_btn_sound / 6))
        self.btn_sound = Button(80,46,self.sf_btn_sound,self.screen)

        # dua vao hinh anh.
        self.sf_btn_mute = image.load('image/musicOff.png')
        self.sf_btn_mute = transform.scale(self.sf_btn_mute, (w_btn_sound / 6, h_btn_sound / 6))



        # tile input name
        title_input_name = "your name: "
        self.sf_title_input_name = StaticView.font_title.render(title_input_name,True,(0,0,0))




        # input - name
        size_input = (140, 60)
        cordinate_input = (310,365)
        self.input_name = pygame_gui.elements.UITextEntryLine(relative_rect=Rect(cordinate_input, size_input),
                                                         manager=self.screen.manager,
                                                         object_id='#input-name')



    def draw_start_game(self):
        self.screen.window.blit(self.sf_bg_start, (0, 0))
        self.btn_start.draw()
        self.btn_rank.draw()
        self.btn_sound.draw()
        self.screen.window.blit(self.sf_title_input_name,(40,380))



    def draw_handle_game(self):
        self.screen.window.blit(self.sf_bg, (0, 0))
