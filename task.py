import cv2
import os


# image_path = os.path.join(os.path.dirname(__file__), 'variant-2.png')
image_path = "d:\\ITMO\\first_year\\Python\\Lab-8\\images\\variant-2.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)qqq
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def image_processing():
    if image is None:
        print("Can not show your photo")
    
    blur_img = cv2.GaussianBlur(image, (5,5), 5)

    #
    edges = cv2.Canny(image, 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    with open("coordinates.txt", 'w') as file:
        for con in contours:
            x, y, w, h = cv2.boundingRect(con)
            file.write(f"x={x}, y={y}, w={w}, h={h}\n")
            if w > 50 and h > 50:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Blur Photo", blur_img)
    cv2.imshow("...", image)

    cv2.waitKey()
    cv2.destroyAllWindows()


def video_processing():
    cam = cv2.VideoCapture(0)
    
    if not cam.isOpened():
        print("Failed to open the camera")
        return
    
    i = 0
    down_point = (640, 480)

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to capture frame")
            break

        frame = cv2.resize(frame, down_point, interpolation=cv2.INTER_LINEAR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        _, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)
        contours, _ =cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) == 0:
            print("No objects detected")

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea) 
            x, y, w, h = cv2.boundingRect(c)
            x_end = min(x + w, frame.shape[1])  # Không vượt quá chiều rộng của khung hình
            y_end = min(y + h, frame.shape[0])  # Không vượt quá chiều cao của khung hình
            # cv2.rectangle(frame, (x,y), (x_end, y_end), (0,255,255), 3)

            scale_factor = 0.8
            new_w = int(w * scale_factor)
            new_h = int(h * scale_factor)
            

            # Tính tọa độ mới để đảm bảo bounding box được thu nhỏ quanh tâm
            new_x = x + (w - new_w) // 2
            new_y = y + (h - new_h) // 2
            cv2.rectangle(frame, (new_x, new_y), (new_x + new_w, new_y +new_h), (0,255,255), 3)

            if i % 5 == 0:
                a = x + w//2
                b = y + h//2
                print(f"Coordinates: {a}, {b}")

        cv2.imshow("Video", frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        i += 1

    cam.release()
    cv2.destroyAllWindows()

def taskExtra():
    # Load the background image and the fly image
    background = cv2.imread(image_path)
    fly = cv2.imread("fly64.png", cv2.IMREAD_UNCHANGED)

    if background is None or fly is None:
        print("Unable to load images")
        return

    # Get image dimensions
    height, width = background.shape[:2]
    im_center = (width//2, height//2)

    # Tìm contour và tâm marker
    edges = cv2.Canny(image, 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        con_center = min(contours, key=lambda con: abs(cv2.pointPolygonTest(con, im_center, True)))
        x, y, w, h = cv2.boundingRect(con_center)
        x_center, y_center = x + w//2, y + h//2
    else:
        print("No contours found!")
        return


    # Get fly image dimensions
    fly_h, fly_w, _ = fly.shape

    x_offset = max(0, min(background.shape[1] - fly_w, x_center - fly_w//2))
    y_offset = max(0, min(background.shape[0] - fly_h, y_center - fly_h//2))


    for y in range(fly_h):
        for x in range(fly_w):
            # Kiểm tra nếu pixel nằm trong giới hạn của ảnh nền
            if (0 <= y + y_offset < background.shape[0] and 0 <= x + x_offset < background.shape[1]):
                # if fly[y, x, 3] != 0:
                #     background[y+y_offset, x+x_offset, :] = fly[y, x, :3]
                if fly.shape[2] == 4 and fly[y, x, 3] != 0:                                 # Check alpha channel
                    background[y + y_offset, x + x_offset] = fly[y, x, :3]
                elif fly.shape[2] == 3:                                                     # If no alpha channel, copy directly
                    background[y + y_offset, x + x_offset] = fly[y, x]



    # Show and save the result
    cv2.imshow("Result", background)
    cv2.imwrite("result.jpg", background)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # taskFirst()

    video_processing()
    taskExtra()