import cv2
import numpy as np
import matplotlib.pyplot as plt


seed = (0,0)


def grown_regionRGB(image, seed=None):

    rows, collums = image.shape[:2] #get the shape of the  image

    xc , yc = seed #get the x clicked and y clicked

    segmented = np.zeros_like(image)

    ref_color = image[xc, yc] # ex :[0, 0 , 255]

    segmented[xc, yc] = ref_color

    
    
    current_found = 0
    previous_points = 1 #set the previous points to 1, so it will enter the while loop
    while previous_points != current_found:
        previous_points = current_found
        current_found = 0
        
        for row in range(rows):
            for col in range(collums):
                if np.array_equal(segmented[row, col], ref_color):
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            nx = row + dx
                            ny = col + dy

                            if 0 <= nx < rows and 0 <= ny < collums:
                                if np.array_equal(image[nx, ny], ref_color) and not np.array_equal(segmented[nx, ny], ref_color):
                                    segmented[nx, ny] = ref_color
                                    current_found += 1

        cv2.imshow("mask", segmented)
        cv2.waitKey(1)
    return segmented

def mouse_callback(event, x, y, flags, param):
        
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed
    
        print(f'The new seed is set to ({y}, {x})')
        seed = (y, x)
        


    


if __name__ == '__main__':

    img = cv2.imread('image.jpg') #read the image

    img = cv2.resize(img , (0, 0), fx=0.3 , fy=0.3) #resizing to execute faster

    segmented = np.zeros_like(img) #creating a mask with the same shape of the image
    cv2.namedWindow('Original image', 1)
    cv2.imshow("Original image", img)
    cv2.setMouseCallback('Original image', mouse_callback)
    cv2.waitKey(0)
    order = 0
    while True:

        

        if cv2.waitKey(1) & 0xFF == ord('c'):
            if seed is not None:
                returned = grown_regionRGB(img, seed)
                segmented += returned
                cv2.imshow("Segmented image", segmented)
                cv2.waitKey(0)
                cv2.destroyAllWindows
                continue
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            print("finalizando...")
            break
    
    

cv2.destroyAllWindows()