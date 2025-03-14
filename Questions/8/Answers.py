import cv2
import numpy as np

Pixels = 5


img = cv2.imread("imagem8.jpg", cv2.IMREAD_COLOR)

if img is None:
    print("the file cannot be read")

else:

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("input gray image", img_gray)
    cv2.imwrite("input_gray_image.jpg", img_gray)
    cv2.imshow("input image", img)
    cv2.imwrite("input_image.jpg", img)

#### i'll resize now

    img_resize1 = cv2.resize(img, (320, 240))
    img_resize2 = cv2.resize(img_resize1, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    img_resize3 = cv2.resize(img_resize2, None, fx= 4.0 , fy= 4.0)

    cv2.imshow("new 320x240px", img_resize1)
    cv2.imshow("new 160x120px", img_resize2)
    cv2.imshow("new 640x480px", img_resize3)
    cv2.imwrite("320x240px.jpg", img_resize1)
    cv2.imwrite("160x120px.jpg", img_resize2)
    cv2.imwrite("640x480px.jpg", img_resize3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    