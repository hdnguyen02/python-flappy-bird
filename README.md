# pygame - Flappy Bird
## Giới thiệu đồ án
- Đồ án game flappy bird xây dựng trên ngôn ngữ lập trình python kết
hợp với thư viện pygame.
## Cơ sở lý thuyết
- Pygame là một tập hợp các module Python được thiết kế để viết game.
Pygame bổ sung chức năng trên thư viện SDL tuyệt vời. Điều này cho phép
bạn tạo các game và chương trình đa phương tiện đầy đủ tính năng bằng
ngôn ngữ python. Pygame có tính di động cao và chạy trên hầu hết mọi
nền tảng và hệ điều hành.
- Pygame được sử dụng rộng rãi và được tải xuống hàng triệu lần.
- Pygame được sử dụng miễn phí. Được phát hành theo giấy phép LGPL,
bạn có thể tạo mã nguồn mở, phần mềm miễn phí, phần mềm chia sẻ và
trò chơi thương mại với nó.
## Tính năng 
### Âm thanh trò chơi
- Khiến game trở nên hấp dẫn đối với người chơi và tạo nên các
khoản khắc. Người chơi có thể bật/tắt âm thanh trong lúc chơi game.

![image](https://github.com/hdnguyen02/python-flappy-bird/assets/83913057/0b9b2846-788d-419f-a4e8-ce4557873269)

### Hiển thị tên và điểm của người chơi xuất sắc nhất
- Hiển thị thông tin của người chơi xuất sắc nhất được ngăn cách
bởi dấu “-“. Với bên trái là user name, bên phải là thành tích của người
chơi đạt được.

    ![image](https://github.com/hdnguyen02/python-flappy-bird/assets/83913057/dca9a9a9-2a96-48b5-8c81-cd711d40f91a)

### Bảng xếp hạng
- Hiển thị bảng xếp hạng giúp người chơi có thể lưu lại thành tích và
chơi cùng với bạn bè. Người chơi phải để lại user name để hệ thống
phân biệt được giữa các người chơi với nhau. Nếu người chơi
không để lại user name thì thành tích của người chơi sẽ không được
ghi nhận tại bảng xếp hạng.
- Bảng xếp hạng hiển thị top 5 người chơi có thành tích tốt nhất. Được
ngăn cách bởi “-“. Bên trái là user name và bên phải là thành tích
của đạt được của người chơi.

    ![image](https://github.com/hdnguyen02/python-flappy-bird/assets/83913057/32fee875-6a86-43e8-8b45-07e569850291)
![image](https://github.com/hdnguyen02/python-flappy-bird/assets/83913057/f8328dbb-500f-4b34-8980-6087ecd729e0)
![image](https://github.com/hdnguyen02/python-flappy-bird/assets/83913057/058b122e-9a2c-4ab5-b796-07979c47599d)

### Chơi game
- Nguời chơi click vào button “Start” để bắt đầu chơi game. Người
chơi sử dụng chuột phải hoặc space để giúp bird không chạm vào sàn,
mép trên cùng và các cột Nếu bird va chạm phải các cột, sàn và mép
trên cùng của cửa sổ game thì trò chơi kết thúc.
![image](https://github.com/hdnguyen02/python-flappy-bird/assets/83913057/5952ef75-b96d-4410-85fe-63c66dcfb7f9)
![image](https://github.com/hdnguyen02/python-flappy-bird/assets/83913057/2e964568-8fcc-4027-af00-a87ed8addd4b)

### Tính điểm
- khi người chơi vượt qua mỗi cặp cột,cột dưới, không đụng sàn
không đụng mép trên cùng điểm của người chơi được cộng thêm 1.
![image](https://github.com/hdnguyen02/python-flappy-bird/assets/83913057/86ba236c-2447-42b6-bf9e-9624088e77a4)

### Kết thúc game
- Sau khi người chơi điều khiển bird va chạm sàn, mép trên cùng
hoặc cột thì game sẽ kết thúc. Hiển thị điểm của người chơi và điểm tốt nhất được ghi nhận.

![image](https://github.com/hdnguyen02/python-flappy-bird/assets/83913057/cacc4d14-9327-4fbe-846e-7886ab1c9f62)

### Chơi thêm hoặc trở về màn hình 
![image](https://github.com/hdnguyen02/python-flappy-bird/assets/83913057/3baaa257-60a4-4d36-be67-eb58af11a49d)






