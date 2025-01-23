import cv2
import numpy as np

img = cv2.imread('imagem2.jpg', cv2.IMREAD_COLOR)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('Window 2')

cv2.imshow('Window 2', img_gray)

cv2.waitKey(0)

cv2.imwrite('imagem2_gray.jpg', img_gray)

cv2.destroyAllWindows()