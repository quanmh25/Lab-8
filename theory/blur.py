# Blur photo (Làm mờ ảnh)

from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
from scipy import ndimage
import cv2
import os 


image_path = "d:\\ITMO\\first_year\\Python\\Lab-8\\theory\\sample.jpg"
# Đường dẫn tương đốiđối
#image_path = os.path.join(os.path.dirname(__file__), 'sample.jpg')


# Làm mờ ảnh rồi hiển thị bằng matplotlibmatplotlib
def blurBymatplot():
    image = Image.open(image_path)

    # Ảnh xám
    gray_img = image.convert('L')

    # Chuyển ảnh xám về mảng
    image_lst = np.array(gray_img)

    # Làm mờ ảnh với bộ lọc Gaussian
    blur_img_a = ndimage.gaussian_filter(image_lst, sigma=0.5, mode="constant")
    blur_img_b = ndimage.gaussian_filter(image_lst, sigma=1, mode="constant")
    blur_img_c = ndimage.gaussian_filter(image_lst, sigma=9, mode="constant")

    # Show photo
    plt.subplot(3,3,1)
    plt.imshow(gray_img, cmap='gray')
    plt.title("Original photo")

    plt.subplot(3,3,3)
    plt.imshow(blur_img_a, cmap='gray')
    plt.title("First blur photo")

    plt.subplot(3,3,7)
    plt.imshow(blur_img_b, cmap='gray')
    plt.title("Second blur photo")

    plt.subplot(3,3,9)
    plt.imshow(blur_img_c, cmap='gray')
    plt.title("Third blur photo")


    plt.show()


# Làm mở ảnh rồi hiển thị bằng opencv
def blurBycv():
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Can't open this file")

    # Cú pháp của hàm GaussianGaussian
    # dst = cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])

    blur_img_a = cv2.GaussianBlur(image, (5,5), 0.5)
    blur_img_b = cv2.GaussianBlur(image, (5,5), 9)

    blur_img_a_mini = cv2.resize(blur_img_a, dsize=None, fx=0.5, fy=0.5)
    blur_img_b_mini = cv2.resize(blur_img_b, dsize=None, fx=0.5, fy=0.5)

    cv2.imshow("First Blur Photo", blur_img_a_mini)
    cv2.imshow("Second Blur Photo", blur_img_b_mini)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    blurBymatplot()
    blurBycv()



