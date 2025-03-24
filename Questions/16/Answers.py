import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img16.jpg", cv2.IMREAD_COLOR)

if img is None:
    print("the file cannot be read")

else:

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("input image", img)
    cv2.imshow("input image in gray scale", img_gray)
    cv2.imwrite("gray_scale_img.jpg" , img_gray)

    # now Equalizating

    img_eq = cv2.equalizeHist(img_gray) 
    cv2.imwrite("Equalizated_image.jpg", img_eq)

    # let's calc the histograms

    original_hist = cv2.calcHist([img_gray], [0], None, [256], [0 , 256])
    equalized_hist = cv2.calcHist([img_eq], [0], None, [256], [0 , 256])

    # now, its grafic time

    plt.figure(1) #creating an default option to my figures

    #ploting histogram of original image

    plt.subplot(2, 2, 1) 
    plt.title('Original Gray Image')
    plt.axis('off')
    plt.imshow(img_gray, cmap='gray')

    #ploting the equalizated image

    plt.subplot(2, 2, 2) 
    plt.title('Equalizated Image')
    plt.axis('off')
    plt.imshow(img_eq, cmap='gray')
    
    #plt.plot example

    plt.subplot(2, 2, 3) 
    plt.plot(original_hist, color='black')
    plt.title('Original Gray Image Histogram')
    plt.xlim(0,256)
    plt.xlabel('Pixels intensity')
    plt.ylabel('Pixels count')

    #plt.hist example

    plt.subplot(2, 2, 4) 
    plt.hist(img_eq.ravel(),  256 , [0,256], color='black')
    plt.title('Equalizated Image Histogram')
    plt.xlim(0,256)
    plt.xlabel('Pixels intensity')
    plt.ylabel('Pixels count')
    

    plt.tight_layout()
    plt.show()
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()