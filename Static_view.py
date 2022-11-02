from pygame import image, transform


class Achievement:
    def __init__(self, screen, font):
        self.screen = screen
        self.score = 0
        self.high_score = 0  # thành tích cao nhất -> tí nũa đọc file
        self.font = font

    def computed_score(self, pipe, bird):  # truyền vào đối tượng chim và đối tượng bird
        left_bird = bird.rect.left
        for obj_pipe in pipe.queue_pipe.queue:
            if obj_pipe["rect_pipe_bottom"].right < left_bird and not obj_pipe["pass"]:
                self.score += 1
                obj_pipe["pass"] = True

    # viết hàm sử dụng điểm vào trong này
    def draw(self, is_play):
        if not is_play:
            return

        surface_score = self.font.render(str(self.score), True, (0, 0, 0))
        rect_surface_score = surface_score.get_rect(center=(self.screen.width / 2, 60))
        self.screen.window.blit(surface_score, rect_surface_score)

    def reset_game(self):
        self.score = 0


class Static_view:

    def __init__(self, screen, path='image/background/bg.jpg'):
        self.screen = screen
        self.sf_bg = transform.scale(image.load(path), (1920, self.screen.height))



    def update_view(self):
        self.screen.window.blit(self.sf_bg, (0,0))


