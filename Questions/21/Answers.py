import cv2
import numpy as np
import sys
sys.path.append('/home/derickbessa/LapiscoTraining/Questions')
from Twenty.functiongr import grown_region



seed = None

def mouse_callback(event, x , y , flags, param):

    global seed

    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'the new seed is setted to ({x} , {y})')
        seed = (x , y)



if __name__ == '__main__':  


    
    img = cv2.imread("image222.jpg", cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscale.jpg", img_gray)

    cv2.namedWindow('Original image', 1)
    cv2.imshow("Original image", img_gray)
    cv2.setMouseCallback("Original image", mouse_callback)

    finish = 0

    while True:

        

        if cv2.waitKey(1) & 0xFF == ord('c'):
            if seed is not None:

                growing_image = grown_region(img_gray, seed)

                cv2.imshow("Segmented image", growing_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows
                continue
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            print("finalizando...")
            break
        
cv2.destroyAllWindows()