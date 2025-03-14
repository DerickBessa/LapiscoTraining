import cv2
import numpy as np

Pixels = 5


img = cv2.imread("imagem6.jpg", cv2.IMREAD_COLOR)

if img is None:
    print("the file cannot be read")

else:

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("input gray image", img_gray)
    cv2.imwrite("input_gray_image.jpg", img_gray)
    cv2.imshow("input image", img)
    cv2.imwrite("input_image.jpg", img)

######## using the canny filter

    edges = cv2.Canny (img_gray, threshold1=100, threshold2=200)
    cv2.imshow("Gray image with edges", edges)
    cv2.imwrite("gray_image_edges.jpg", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows