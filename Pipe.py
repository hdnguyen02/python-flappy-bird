from random import randrange
from Floor import Floor
from View import Screen
from pygame import USEREVENT, time, image, transform, KEYDOWN, K_SPACE, MOUSEBUTTONDOWN


class Pipe:
    width, height = 60, 360
    min_y = 160
    surface_bottom = transform.scale(image.load('image/pipe/pipe.png'), (width, height))
    surface_top = transform.flip(surface_bottom, False, True)
    start_y_random = Screen.height - Floor.height + 10
    end_y_random = start_y_random + height - min_y
    previous_y = None # luu tru lan random truoc.
    step = 50
    # khởi tạo sự kiện cho pipe
    event_pipe = USEREVENT
    repeat_time = 1800  # 1200 giây là xuất hiện trụ
    time.set_timer(event_pipe, repeat_time)
    blank = 160  # khoản hở giữa 2 trụ
    distance = 220  # khoản cách giữa các trụ
    speed = 2

    def __init__(self):
        self.list_pipe = []  # khởi tạo pipe
        self.__is_play = True # đánh dấu trạng thái vẫn còn hoạt động.

    # các hàm seter
    # tạo hàm get
    @property
    def is_play(self):
        return self.__is_play

    @is_play.setter
    def is_play(self,status):
        self.__is_play = status

    def handle_event(self, sub_event):
        if sub_event.type == Pipe.event_pipe:
            self.add_random_pipe()
        elif ((sub_event.type == KEYDOWN and sub_event.key == K_SPACE) or (sub_event.type == MOUSEBUTTONDOWN)) and not self.__is_play:
            self.reset_game()

    def move_pipe(self):
        for pipe in self.list_pipe:
            pipe.centerx -= Pipe.speed

    def draw(self, window):
        # game còn hoạt động mới vẽ ra
        if not self.__is_play:
            return
        self.move_pipe()
        for pipe in self.list_pipe:
            if pipe.top < 0:
                window.blit(Pipe.surface_top, pipe)
            else:
                window.blit(Pipe.surface_bottom, pipe)

    def reset_game(self):
        self.__is_play = True
        self.list_pipe.clear()

    def add_random_pipe(self):
        while True:
            y_random = randrange(Pipe.start_y_random, Pipe.end_y_random, Pipe.step)
            if y_random != Pipe.previous_y:
                Pipe.previous_y = y_random
                break
        rect_pipe_bottom = Pipe.surface_bottom.get_rect(midbottom=(560, y_random))
        rect_pipe_top = Pipe.surface_bottom.get_rect(midbottom=(560, y_random - Pipe.height - Pipe.blank))
        self.list_pipe.extend([rect_pipe_bottom, rect_pipe_top])
