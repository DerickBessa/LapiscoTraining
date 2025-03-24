import cv2
import numpy as np
from numba import njit 

@njit
def grown_region(image , seed=None):
    
    rows, cols = image.shape[:2]
    region = np.zeros_like(image)
    xc, yc = seed

    region[xc, yc] = 255

    directions = [(-1 , -1),(-1 , 0),(-1 , 1),(0 , -1), (0 , 1), (1 , -1), (1 , 0), (1 , 1)]

    previous_point = 1
    current_found = 0

    while previous_point != current_found:  #if the list is not empty, will keep continue
    

        for row in range(rows):   ## for one of all pixel in this image...
            for col in range (cols):## ...

                #will make this

                for dx, dy in directions:
                    nx , ny = row + dx , col + dy  # i use the sum, cuz when you sum x + (-1) and y + (-1), for example, u can get the before row and before collum, and this is an 3x3 kernel with 5 diferent directions 
                    
                    if 0 <= nx < image.shape[0] and 0<= ny< image.shape[1]:
                        if  image[nx,ny] < 127 and region[nx, ny] == 0:
                            region[nx,ny] = 255
                            current_found = 1

                

        return region

img = cv2.imread("image.jpg", cv2.IMREAD_COLOR)

if img is None:
    print("the file cannot be read")

else:

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("input image", img)
    cv2.imshow("input image in gray scale", img_gray)
    cv2.imwrite("gray_scale_img.jpg" , img_gray)

    seed = (img_gray.shape[0] //2 , img_gray.shape[1] // 2)

    img_growing_mask = grown_region(img_gray, seed)

    cv2.imshow("Imagem with growing mask", img_growing_mask)
    cv2.imwrite("img_grow_mask.jpg", img_growing_mask)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


