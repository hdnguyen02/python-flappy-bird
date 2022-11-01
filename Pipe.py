from random import randrange
from Floor import Floor
from View import Screen
from pygame import USEREVENT, time, image, transform
from queue import Queue


# ý tưởng: chỉ có 3 pipe được tạo ra. -> sau đó thay phiên vẽ lại 3 cây trụ này
# xác định witdh height của chương trình


class Pipe:
    width, height = 60, 360
    min_y = 160
    surface_bottom = transform.scale(image.load('image/pipe/pipe.jpg'), (width, height))
    surface_top = transform.flip(surface_bottom, False, True)
    start_y_random = Screen.height - Floor.height + 10
    end_y_random = start_y_random + height - min_y
    previous_y = None  # luu tru lan random truoc.
    step = 50
    speed = 2  # tốc độ di chuyển.
    # khởi tạo sự kiện cho pipe
    event_pipe = USEREVENT
    repeat_time = 2000  # 1200 giây là xuất hiện trụ
    time.set_timer(event_pipe, repeat_time)
    blank = 160  # khoản hở giữa 2 trụ

    def __init__(self):
        self.queue_pipe = Queue()  # khởi tạo queue -> tí dễ xóa cái đầu tiên.
        self.pipe_pass = 0

    def handle_create_pipe(self, sub_event):
        if sub_event.type == Pipe.event_pipe:
            self.add_random_pipe()

    def __check_number_pipe(self):
        if self.queue_pipe.qsize() > 3:
            self.queue_pipe.get()

    def __move_pipe(self):
        right_bird = 100
        for pipe in self.queue_pipe.queue:
            # kiểm tra xem trụ đã qua chưa.
            if pipe["rect_pipe_bottom"].right < right_bird and not pipe["pass"]:
                self.pipe_pass += 1
                pipe["pass"] = True
            pipe["rect_pipe_bottom"].centerx -= Pipe.speed
            pipe["rect_pipe_top"].centerx -= Pipe.speed

    def draw(self, window, is_play):
        if not is_play:
            return
        self.__check_number_pipe()
        self.__move_pipe()
        for pipe in self.queue_pipe.queue:
            window.blit(Pipe.surface_top, pipe["rect_pipe_top"])
            window.blit(Pipe.surface_bottom, pipe["rect_pipe_bottom"])

    def reset_game(self):
        self.pipe_pass = 0
        while not self.queue_pipe.empty():
            self.queue_pipe.get()

    def add_random_pipe(self):
        while True:
            y_random = randrange(Pipe.start_y_random, Pipe.end_y_random, Pipe.step)
            if y_random != Pipe.previous_y:
                Pipe.previous_y = y_random
                break
        rect_pipe_bottom = Pipe.surface_bottom.get_rect(midbottom=(560, y_random))
        rect_pipe_top = Pipe.surface_bottom.get_rect(midbottom=(560, y_random - Pipe.height - Pipe.blank))
        dict_pipe = {
            "pass": False,
            "rect_pipe_bottom": rect_pipe_bottom,
            "rect_pipe_top": rect_pipe_top
        }
        self.queue_pipe.put(dict_pipe)
