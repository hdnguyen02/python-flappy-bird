from pygame import mixer, init, font

init()


class Achievement:
    sound_pass = mixer.Sound('sound/congdiem.mp3')
    font_show_user = font.Font('font/show-user.ttf', 36)

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.name = None  # kiem tra neu nguoi dung khong nhap ten -> thi cho choi nhung khong xep hang.
        self.top_5_user = [
            # dict(name="duc nguyen", core=100),
            # dict(name="xuan hanh", core=94),
            # dict(name="thanh van", core=93),
            # dict(name="thanh nhat", core=12),
            # dict(name="thai cong", core=2)
        ]  # là 1 cái mang chưa thông tin của 10 người choi cao nhat
        # ai chơi lọt top 10 sẽ được lưu tên + thành tích lại


        self.read_file_top()

    def handle_sign_in(self, name):
        if name.strip() != '':
            self.name = name  # gán tên cho thằng này.



    @staticmethod
    def my_compare(user):
        return user["core"]

    def handle_die(self):
        if self.name and self.score >= self.top_5_user[4]["core"]:
            print('tiến hành so sánh')
            self.top_5_user.append(dict(name=self.name, core=self.score))
            self.top_5_user.sort(key=Achievement.my_compare, reverse=True)
            self.top_5_user.pop(len(self.top_5_user) - 1)
            self.ghi_file()

    def draw_start_game(self):
        font_show_top = font.Font('font/show-user.ttf', 26)
        title = "top 1: " + self.top_5_user[0]["name"] + "-" + str(self.top_5_user[0]["core"])
        sf_high_user = font_show_top.render(title, True, (0, 0, 0))
        rect_sf_high_user = sf_high_user.get_rect(center=(self.screen.width // 2, 300))
        self.screen.window.blit(sf_high_user, rect_sf_high_user)

    def write_file(self):
        pass

    def computed_score(self, pipe, bird, is_sound):  # truyền vào đối tượng chim và đối tượng bird
        left_bird = bird.rect.left
        for obj_pipe in pipe.queue_pipe.queue:
            if obj_pipe["rect_pipe_bottom"].right < left_bird and not obj_pipe["pass"]:
                if is_sound:
                    Achievement.sound_pass.play()
                self.score += 1
                obj_pipe["pass"] = True

    # viết hàm sử dụng điểm vào trong này
    def draw_handle_game(self, is_play):
        if not is_play:
            return
        margin_left = 26
        surface_score = Achievement.font_show_user.render(str(self.score), True, (0, 0, 0))
        if self.name != None:
            sf_user = Achievement.font_show_user.render(self.name + ": ", True, (0, 0, 0))
            self.screen.window.blit(sf_user, (margin_left, 26))
            self.screen.window.blit(surface_score, (margin_left + sf_user.get_width() + 6, 26))
        else:
            self.screen.window.blit(surface_score, (margin_left + 6, 26))

    def reset_game(self):
        self.score = 0

    def read_file_top(self):
        # đọc vào file top
        # nén hai cái lại rồi rồi lặp qua.
        for line in open('top.txt','r'):
            name, score =  line.rstrip().split('-')
            score = int(score)
            self.top_5_user.append(dict(name=name,core=score))

    # viet 1 ham ghi lai file
    def ghi_file(self):
        file = open('top.txt','w')
        temp = []
        for x in self.top_5_user:
            t = x['name'] + '-' + str(x['core']) + '\n'
            print(t)
            temp.append(t)

        file.writelines(temp)

