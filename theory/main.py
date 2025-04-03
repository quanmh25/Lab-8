

import cv2
import imutils

storage = "d:\\ITMO\\first_year\\Python\\Lab-8\\theory\\"


def readPhotos():
    # Đọc ảnh (Từ thư mục)
    read_pic = cv2.imread(f"{storage}sample.jpg", cv2.IMREAD_GRAYSCALE)      # Màu trắng đen

    # Hiển thị ảnh
    cv2.imshow("Name of window", read_pic)
    cv2.resizeWindow("Name of window", 1000, 1000)       # resize photo

    # New window for showing mini photo
    mini_pic = cv2.resize(read_pic, dsize=None, fx=0.5, fy=0.5)
    cv2.imshow("Mini Pic", mini_pic)

    # Ghi file
    cv2.imwrite(f"{storage}newpic.jpg", mini_pic)

    # Xoay ảnh ( To rotate a photo)
    rot_pic = imutils.rotate(mini_pic, 90)
    cv2.imshow("Rotate", rot_pic)

    # Dừng chương trình
    cv2.waitKey()
    cv2.destroyAllWindows()



# Lấy ngưỡng ảnh -> chuyển ảnh xám thành ảnh nhị phân
def threshBin():
    # original photo
    ori_pic = cv2.imread(f"{storage}sample.jpg", cv2.IMREAD_GRAYSCALE)
    if ori_pic is None:
        print("Impossible to open photo")
        return

    # Ngưỡng tự chọn
    thresh_val = 127    # Giá trị ngưỡng (threshold value).            
    max_val = 255       # Giá trị gán cho các pixel vượt ngưỡng.

    # Hàm cv2.threshold() trong OpenCV trả về hai giá trị: ret và bin_pic
    ret, bin_pic = cv2.threshold(ori_pic, thresh_val, max_val, cv2.THRESH_BINARY)           # ret sẽ chứa giá trị ngưỡng (127).  
    #cv2.imshow("Binary photo", bin_pic)                                                     # bin_pic sẽ chứa ảnh nhị phân sau khi áp dụng ngưỡng nhị phân.
    mini_bin = cv2.resize(bin_pic, dsize=None, fx=0.5, fy=0.5)
    cv2.imshow("Mini Binary Photo", mini_bin)

    # Hàm Adaptive Threshold chọn ngưỡng động trong vùng lân cận -> hiệu quả hơn việc chọn thresh_valval
    res_pic = cv2.adaptiveThreshold(ori_pic, max_val, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 5)
    cv2.imshow("Result Pic", res_pic)

    cv2.waitKey()
    cv2.destroyAllWindows()


def readCam():
    # Open webcam
    cam_id = 0        # Number from 0 -> n, to mark webcam
    cam = cv2.VideoCapture(cam_id)

    # Đọc ảnh liên tục từ camera
    while True:
        ret, frame = cam.read()
        if ret: 
            cv2.imshow("Webcam", frame)
            # Viết code ở đây để xử lý thêm hoặc truyền vào model deep learning

        if cv2.waitKey(1) == ord('q'):
            break
    
    cam.release()
    cv2.destroyAllWindows()


def readVid():
    vid_file = "d:\\ITMO\\first_year\\Python\\Lab-8\\theory\\story.mp4"
    cam = cv2.VideoCapture(vid_file)
    while True:
        ret, frame = cam.read()
        if ret:
            cv2.imshow("video", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cam.destroyAllWindows()


if __name__ == '__main__':
    # readPhotos()
    threshBin()         # Lấy ngưỡng

    # readCam()
    # readVid()