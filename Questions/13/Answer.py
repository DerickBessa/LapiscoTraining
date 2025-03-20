import cv2
import numpy as np

img = cv2.imread("car.jpg", cv2.IMREAD_COLOR)

if img is None:
    print("the file cannot be read")

else:

    img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

    cv2.imshow("input image", img)
    cv2.imshow("grays scaled input image", img_gray)
    cv2.imwrite("gray_scale_inpIMG.jpg", img_gray)
    
    static_matrix = np.zeros_like(img_gray)

    # first way, basically is this:

    '''sobel_X = np.array([[-1 , 0 , +1],
                                [-2 , 0 , +2],
                                [-1 , 0 , +1]])
     
    sobel_Y = np.array([[-1 , -2 , -1],
                                [ 0  , 0 ,  0],
                                [+1 , +2 , +1]])

        #and after this i could use this
for i in range(1, img_gray.shape[0] - 1):
    for j in range(1, img_gray.shape[1] - 1): 
        region = img_gray[i-1:i+2, j-1:j+2]
        
        gx = np.sum(region * sobel_X)
        gy = np.sum(region * sobel_Y)

        gr = np.sqrt(gx**2 + gy**2)

        static_matrix[i, j] = np.uint8(np.clip(gr, 0, 255))'''
     
                    
     #i will make now in faster way   - second way

    gx = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0 , ksize=3) ### this function do the convolution applying the sobels mask
    gy = cv2.Sobel(img_gray, cv2.CV_64F, 0 , 1 , ksize=3)

    ##now i will merge the gradients

    gr = np.sqrt(gx**2 + gy**2)

    static_matrix = np.uint8(np.clip(gr, 0 , 255)) ### i did this, 'cause, when u get the CV_64F format you maybe work with values upper and lower than 255 and 0. 
            ## and with this im normalizing to [0 , 255]

           
           
cv2.imshow("input image with sobels mask", static_matrix)
cv2.imwrite("Sobels_mask.jpg", static_matrix)
cv2.waitKey(0)
cv2.destroyAllWindows()