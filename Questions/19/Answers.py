import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img19.jpg", cv2.IMREAD_COLOR)

if img is None:
    print("the file cannot be read")

else:

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("input image", img)
    cv2.imshow("input image in gray scale", img_gray)
    cv2.imwrite("gray_scale_img.jpg" , img_gray)


    gradient_x = cv2.Sobel(img_gray, cv2.CV_64F, 1 , 0 ,ksize=3) #sobel x
    gradient_y = cv2.Sobel(img_gray, cv2.CV_64F, 0 , 1 ,ksize=3) #sobel y

    gr = np.sqrt(gradient_x**2 + gradient_y**2)

    Sobels_image = cv2.convertScaleAbs(gr)

    plt.figure(figsize=(10,10))

    plt.subplot(2,2,1)
    plt.title('original image')
    plt.imshow(img_gray,cmap='gray')
    plt.axis('off')

    plt.subplot(2,2,2)
    plt.title('Solbelized image')
    plt.imshow(Sobels_image,cmap='gray')
    plt.axis('off')

    plt.subplot(2,2,3)
    plt.hist(img_gray.ravel(), 256 ,[0,256], color='red' )
    plt.xlim(0 , 256)
    plt.xlabel('Pixels Intensity')
    plt.ylabel('Pixels Count')


    plt.subplot(2,2,4)
    plt.hist(Sobels_image.ravel(), 256 ,[0,256], color='red' )
    plt.xlim(0 , 256)
    plt.xlabel('Pixels Intensity')
    plt.ylabel('Pixels Count')


    plt.tight_layout()
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()