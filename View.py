from pygame import image, init, display, transform, font, time, Surface


class Font:
    font.init()
    font_score = font.Font('font/TypefaceMario64-ywA93.otf', 40)



class Screen:
    width = 500
    height = 700
    size = (width, height)
    window = display.set_mode(size)


class Achievement:
    def __init__(self):
        self.score = 0
        self.high_score = 0  # thành tích cao nhất -> tí nũa đọc file

    # viết hàm set điểm
    def computed_score(self, pipe, bird):  # truyền vào đối tượng chim và đối tượng bird
        left_bird = bird.rect.left
        for obj_pipe in pipe.queue_pipe.queue:
            if obj_pipe["rect_pipe_bottom"].right < left_bird and not obj_pipe["pass"]:
                self.score += 1
                obj_pipe["pass"] = True

    # viết hàm sử dụng điểm vào trong này
    def draw(self, window, is_play):
        if not is_play:
            pass

        surface_score = Font.font_score.render(str(self.score), True, (0, 0, 0))
        rect_surface_score = surface_score.get_rect(center=(Screen.width / 2, 60))
        window.blit(surface_score, rect_surface_score)

    def draw_game_over(self, window):
        fps = 120
        clock = time.Clock()

        surface = image.load('image/bird/0.png')
        w, h = Surface.get_size(surface)
        surface = transform.scale(surface, (w / 15, h / 15))
        for i in range(100):
            clock.tick(fps)
            rect = surface.get_rect(center=(Screen.width / 2, i))

            window.blit(surface, rect)
            display.update()

    def reset_game(self):
        self.score = 0


class View:
    # load vao button game
    surface_btn_start = image.load('image/button/start-removebg-preview.jpg')  # load vao anh

    w_btn_start, h_btn_start = surface_btn_start.get_size()
    scale_btn_start = 4
    surface_btn_start = transform.scale(surface_btn_start,
                                        (w_btn_start / scale_btn_start, h_btn_start / scale_btn_start))
    rect_btn_start = surface_btn_start.get_rect(center=(Screen.width / 2, 600))

    # load image start game
    surface_bg_start = image.load('image/background/bg-start.jpg')
    surface_bg_start = transform.scale(surface_bg_start, (1920, Screen.height))

    # title input.
    title_input = "your name"
    # load chu tai day.
    # render ra
    surface_title = Font.font_score.render(title_input,True, (0, 0, 0))
    rect_title = surface_title.get_rect(center = (Screen.width / 2, 200))


    # load vao o nhap ten nguoi dung
    surface_input = image.load('image/input/input-name.jpg')

    rect_input = surface_input.get_rect(center=(Screen.width / 2, 300))

    def __init__(self):
        init()
        self.bg = image.load('image/background/bg.jpg')
        self.bg = transform.scale(self.bg, (1920, Screen.height))
        display.set_caption('Flappy Bird')
        self.core = 0  # biến hiển thị điểm.

    # thiết kế hiên thị điểm tại view
    def display_score(self, pipe, bird):
        left_bird = bird.rect.left
        for obj_pipe in pipe.queue_pipe.queue:
            if obj_pipe["rect_pipe_bottom"].right < left_bird and not obj_pipe["pass"]:
                self.core += 1
                obj_pipe["pass"] = True
            # ý tưởng : tao form o nhap cho nguoi dung nhap ten vao.

    # cần viết 1 hàm show test người dùng nhập được len.
    def handle_view_start_game(self):
        Screen.window.blit(View.surface_bg_start, (0, 0))
        Screen.window.blit(View.surface_btn_start, View.rect_btn_start)
        Screen.window.blit(View.surface_input, View.rect_input)
        Screen.window.blit(View.surface_title, View.rect_title)

        display.update()

    def update(self, is_play, *args):  # để có thể sử lấy ra các biến trong control.
        Screen.window.blit(self.bg, (0, 0))
        for sub in args:
            sub.draw(Screen.window, is_play)
        display.update()

    def screen_finish_game(self, *agrs):
        for sub in agrs:
            sub.draw_game_over(Screen.window)

        display.update()
