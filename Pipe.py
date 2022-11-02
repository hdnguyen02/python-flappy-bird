from random import randrange
from Floor import Floor
from pygame import USEREVENT, time, image, transform
from queue import Queue


class Pipe:
    min_y = 160
    width, height = 60, 360
    sf_bottom = transform.scale(image.load('image/pipe/pipe.jpg'), (width, height))
    sf_top = transform.flip(sf_bottom, False, True)
    speed = 2
    repeat_time = 2000
    event_pipe = USEREVENT + 6
    time.set_timer(event_pipe, repeat_time)
    blank = 160

    def __init__(self, screen):

        self.screen = screen
        self.start_y_rd = self.screen.height - Floor.height + 10
        self.end_y_rd = self.start_y_rd + Pipe.height - Pipe.min_y
        self.step_rd = 50
        self.previous_y = None

        self.queue_pipe = Queue()  # khởi tạo queue -> tí dễ xóa cái đầu tiên.

    def handle_create_pipe(self, sub_event):
        if sub_event.type == Pipe.event_pipe:
            self.add_random_pipe()

    def __check_number_pipe(self):
        if self.queue_pipe.qsize() > 3:
            self.queue_pipe.get()

    def __move_pipe(self):
        for pipe in self.queue_pipe.queue:
            pipe["rect_pipe_bottom"].centerx -= Pipe.speed
            pipe["rect_pipe_top"].centerx -= Pipe.speed

    def draw_handle_game(self, is_play):
        if not is_play:
            return
        self.__check_number_pipe()
        self.__move_pipe()
        for pipe in self.queue_pipe.queue:
            self.screen.window.blit(Pipe.sf_top, pipe["rect_pipe_top"])
            self.screen.window.blit(Pipe.sf_bottom, pipe["rect_pipe_bottom"])

    def reset_game(self):
        while not self.queue_pipe.empty():
            self.queue_pipe.get()

    def add_random_pipe(self):
        while True:
            y_random = randrange(self.start_y_rd, self.end_y_rd, self.step_rd)
            if y_random != self.previous_y:
                self.previous_y = y_random
                break
        rect_pipe_bottom = Pipe.sf_bottom.get_rect(midbottom=(560, y_random))
        rect_pipe_top = Pipe.sf_bottom.get_rect(midbottom=(560, y_random - Pipe.height - Pipe.blank))
        dict_pipe = {
            "pass": False,
            "rect_pipe_bottom": rect_pipe_bottom,
            "rect_pipe_top": rect_pipe_top
        }
        self.queue_pipe.put(dict_pipe)
