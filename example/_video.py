import time

import cv2

def video_processing():
    cap = cv2.VideoCapture(0)

    # cv2.VideoCapture(0) không bao giờ trả về None
    if not cam.isOpened():
        raise IOError("Failed to open the camera")
    
    
    down_points = (640, 480)            # resize khung hinh -> giup toc do xu ly nhanh hon
    
    i = 0       # Đếm số khung hình đã xử lý -> in tọa độ sau mỗi vài khung hình
    while True:
        ret, frame = cap.read()         # Doc tung khung hinh
        if not ret:             # ret tra ve True vaf False, frame luu du lieu anh cua khung hinh
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)              # chuyen ve mau xam
        gray = cv2.GaussianBlur(gray, (21, 21), 0)                  # lam mo anh

        # Phat hien doi tuong
        ret, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,                  # Lấy contour ngoài cùng của các đối tượng (bỏ qua các contour bên trong)
            cv2.CHAIN_APPROX_SIMPLE             # Lưu các điểm cần thiết trên contour để tiết kiệm bộ nhớ
        )

        # xác định đối tượng lớn nhất
        if len(contours) > 0:           # Kiểm tra contour
            c = max(contours, key=cv2.contourArea)      # Lấy contour lớn nhất
            x, y, w, h = cv2.boundingRect(c)            # Trả về tọa độ trên bên trái, chiều rộng và cao của hình như nhật
            # Vẽ hình chữ nhật màu xanh lá cây lên khung hình lớn nhất
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)    # Trong hàm cv2.rectangle, số 2 là tham số xác định độ dày của đường viền hình chữ nhật. (2pixel)
                                                                        # Nếu đặt tham số này thành -1, hình chữ nhật sẽ được tô đầy bên trong
            # In tọa độ mỗi 5 khung hình
            if i % 5 == 0:
                a = x + (w // 2)   # Tọa độ tâm
                b = y + (h // 2)
                print(a, b)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()


if __name__ == '__main__':
    video_processing()

# cv2.waitKey(0)
# cv2.destroyAllWindows()






# VẼ MÀU CHO KHUNG HÌNH CHỮ NHẬTNHẬT
# Màu đỏ: (0, 0, 255)

# Màu xanh lá cây: (0, 255, 0)

# Màu xanh dương: (255, 0, 0)

# Màu vàng: (0, 255, 255) (Green + Red)

# Màu tím: (255, 0, 255) (Blue + Red)

# Màu trắng: (255, 255, 255) (Blue + Green + Red)

# Màu đen: (0, 0, 0) (Không có màu nào cả)

# Màu cam: (0, 165, 255) (Green + Red)