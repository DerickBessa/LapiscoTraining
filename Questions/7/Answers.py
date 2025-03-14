import cv2
import numpy as np

Pixels = 5


img = cv2.imread("imagem7.jpg", cv2.IMREAD_COLOR)

if img is None:
    print("the file cannot be read")

else:

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("input gray image", img_gray)
    cv2.imwrite("input_gray_image.jpg", img_gray)
    cv2.imshow("input image", img)
    cv2.imwrite("input_image.jpg", img)

    ##### thresholding
    
    threshold_min = 165 ##### for more, + black, for low, + white
    threshold_max = 255

    limiar_ignore , thresholded_img = cv2.threshold(img_gray, threshold_min, 255, cv2.THRESH_BINARY)


    cv2.imshow("thresholded image", thresholded_img)
    cv2.imwrite("thresholded_image.jpg", thresholded_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()