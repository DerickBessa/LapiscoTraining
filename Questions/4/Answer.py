import cv2
import numpy as np

img = cv2.imread('imagem4.jpg', cv2.IMREAD_COLOR)

if img is None:

    print("the file cannot be read")

else:
    
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #conversion

    R , G , B = cv2.split(img)  # spliting channels

    ######### now i'll create 1 image for 1 channel

    R_img = cv2.merge([np.zeros_like(B), np.zeros_like(G), R])#in BGR format
    G_img = cv2.merge([np.zeros_like(B), B, np.zeros_like(R)])
    B_img = cv2.merge([B, np.zeros_like(G), np.zeros_like(R)])

    ################################ now we have the same image in 3 different channels

    cv2.imshow('RED CHANNEL', R_img)
    cv2.imshow('GREEN CHANNEL', G_img)
    cv2.imshow('BLUE CHANNEL', B_img)
    cv2.imshow('IMAGE HSV.jpg', img_HSV)

    ##################### now, let's save it

    cv2.imwrite('red_channel.jpg', R_img)
    cv2.imwrite('green_channel.jpg', G_img)
    cv2.imwrite('blue_channel.jpg', B_img)
    cv2.imwrite('hsv_img.jpg', img_HSV)

    cv2.waitKey(0)
    cv2.destroyAllWindows