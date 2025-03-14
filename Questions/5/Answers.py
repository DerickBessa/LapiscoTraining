import cv2
import numpy as np

Pixels = 5

### def functions
def cv_median(image, kernel_size):
    median_blur_image = cv2.medianBlur(image, kernel_size)
    return median_blur_image

def cv_blur(image, kernel_row_size, kernel_colum_size):
    blur_image = cv2.blur(image,(kernel_row_size, kernel_colum_size))
    return blur_image


####### opening an colored image

img = cv2.imread('imagem5.jpg', cv2.IMREAD_COLOR)

if img is None:

    print("the file cannot be read")

else:            ##### now i'll convert to gray

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("input gray image", img_gray)
    cv2.imwrite("input_gray_image.jpg", img_gray)
    cv2.imshow("input image", img)
    cv2.imwrite("input_image.jpg", img)

    ####### now i will use the media blur in 'input_gray_image'

    img_blur = cv_blur(img_gray, Pixels , Pixels)

    cv2.imshow("input gray image with blur", img_blur)
    cv2.imwrite("blur_input_gray_image.jpg", img_blur)

    img_medianBlur = cv_median(img_gray , Pixels)

    cv2.imshow("input gray image with medianBlur", img_medianBlur)
    cv2.imwrite("medianBlur_input_gray_image.jpg", img_medianBlur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()