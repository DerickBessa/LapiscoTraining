import cv2
import numpy as np

img = cv2.imread('imagem1.jpg', cv2.IMREAD_COLOR)

if img is None:
    print("a imagem não pode ser lida")
    
else:
    cv2.namedWindow('Hello World')

    cv2.imshow('Hello World', img)

    cv2.waitKey(0) ## impede que a imagem apenas pisque na tela

    cv2.imwrite('imagem1.jpg', img)

    cv2.destroyAllWindows()
