from pygame import time, event, QUIT, quit, KEYDOWN
from View import View
from Floor import Floor
from Bird import Bird
from Pipe import Pipe


class Control:
    def __init__(self, fps=60):
        self.fps = fps
        self.clock = time.Clock()
        self.is_play = True # game còn chơi.

        self.floor = Floor()
        self.view = View()
        self.bird = Bird()
        self.pipe = Pipe()
        self.run = True


    # viết 1 hàm -> hàm này tạo ra vòng lặp sự kiê

    def play_game(self):
        while self.run:
            self.clock.tick(self.fps)
            for sub_event in event.get():
                if sub_event.type == QUIT:
                    self.run = False
                self.bird.handle_event(sub_event)
                self.pipe.handle_event(sub_event)
            self.view.update(self.pipe, self.floor, self.bird)
            # khi game kết thúc -> vẫn cho chạy game -> game vẫn chạy.

            self.bird.is_play = not self.bird.is_collision(self.pipe)
            self.pipe.is_play = not self.bird.is_collision(self.pipe)


            # gọi hàm xử lý kết thúc.
        quit()

    # xem lại code phần rect của floor

