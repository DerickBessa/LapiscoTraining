import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img17.jpg", cv2.IMREAD_COLOR)

if img is None:
    print("The file cannot be read")

else:

    img_gray = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY)

    cv2.imshow("input image", img)
    cv2.imshow("gray scale input image", img_gray)
    cv2.imwrite("img_gray.jpg", img_gray)

    ### now i will make the equalizator

    def calc_hist(img_array):

        #creating an matrix of 0 in 256 levels of pixels (0 ,255)

        histogram = np.zeros(256, dtype=int)

        #transforming the image in 1D to get vector of number

        for pixel in img_array.flatten():
            histogram[pixel] +=1

        return histogram  
    
    histogram = calc_hist(img_gray)

    cdf = np.zeros_like(histogram)

    for i in range(len(histogram)):
        if i == 0:
            cdf[i] = histogram[0]
        else:
            cdf[i] = histogram[i] + cdf[i-1]
        
    #normalizing the cdf for (0,255)
    normalizated_cdf = cdf.astype('uint8')

    #using cdf like a list of values to change the pixels value of original image

    equalizated_img = normalizated_cdf[img_gray.flatten()]

    equalizated_img = np.reshape(equalizated_img, img_gray.shape)

    # now i'll create the grafics

    plt.figure(1)

    #ploting original image

    plt.subplot(2,2,1)
    plt.title(' Original Gray Image')
    plt.axis('off')
    plt.imshow(img_gray, cmap='gray')

    #ploting equalizated img

    plt.subplot(2,2,2)
    plt.title('Equalizated Image')
    plt.axis('off')
    plt.imshow(equalizated_img, cmap='gray')

    #ploting original image histogram

    plt.subplot(2,2,3)
    plt.hist(img_gray.ravel(), 256 , [0,256], color='black')
    plt.title('Original Gray image histogram')
    plt.xlim(0,256)
    plt.xlabel('Pixels Intensity')
    plt.ylabel('Pixels Count')

    #ploting equalizated image histogram

    plt.subplot(2,2,4)
    plt.hist(equalizated_img.ravel(), 256 , [0,256], color='black')
    plt.title('Original Gray image histogram')
    plt.xlim(0,256)
    plt.xlabel('Pixels Intensity')
    plt.ylabel('Pixels Count')

    plt.tight_layout()
    plt.show()

