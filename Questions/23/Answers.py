import cv2
import numpy as np
import matplotlib.pyplot as plt


seed = (0,0)


def grown_region(image, seed=None):

    rows, collums = image.shape[:2] #get the shape of the  image

    xc , yc = seed #get the x clicked and y clicked

    mask = np.zeros_like(image)
    mask[xc, yc] = 255 #marking the seed point  in the image

    directions = [(-1 , -1),(-1 , 0),(-1 , 1),(0 , -1), (0 , 1), (1 , -1), (1 , 0), (1 , 1)]

    
    current_found = 0
    previous_points = 1 #set the previous points to 1, so it will enter the while loop
    while previous_points != current_found:
        previous_points = current_found
        current_found = 0

        for row in range(rows):
            for col in range(collums):
                if mask[row, col] == 255: #if the pixel is already in the region
                    for dx, dy in directions:
                        nx , ny = row + dx , col + dy
                        

                        if 130 < image[nx,ny] < 230:
                            mask[nx,ny] = 255
                            current_found += 1

    return mask
def mouse_callback(event, x, y, flags, param):
        
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed
    
        print(f'The new seed is set to ({x}, {y})')
        seed = (x, y)
        


    


if __name__ == '__main__':

    img = cv2.imread('image.jpg', cv2.IMREAD_COLOR) #read the image
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('Original image', 1)
    cv2.imshow("Original image", img_gray)
    cv2.setMouseCallback('Original image', mouse_callback)
    cv2.waitKey(0)

    segmented_image = grown_region(img_gray, seed)

    cv2.imshow("Segmented image", segmented_image)
    cv2.waitKey(0)
    

cv2.destroyAllWindows()