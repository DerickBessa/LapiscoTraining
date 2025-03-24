import cv2
import numpy as np

img = cv2.imread("img18.jpg", cv2.IMREAD_COLOR)

if img is None:
    print("the file cannot be read")

else:

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("input image", img)
    cv2.imshow("input image in gray scale", img_gray)
    cv2.imwrite("gray_scale_img.jpg" , img_gray)


    laplacian = cv2.Laplacian(img_gray, cv2.CV_64F, ksize=3)

    laplacian = cv2.convertScaleAbs(laplacian)

    cv2.imshow("Laplacian image", laplacian)
    cv2.imshow("laplacian_image.jpg", laplacian)

    equalizated_laplacian = cv2.equalizeHist(laplacian)

    cv2.imshow("Equalizated Laplacian Image", equalizated_laplacian)
    cv2.imwrite("eq_laplacian_img.jpg", equalizated_laplacian)

    cv2.waitKey(0)
    cv2.destroyAllWindows