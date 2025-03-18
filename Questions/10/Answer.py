import cv2
import numpy as np

img = cv2.imread("imagem10.jpg", cv2.IMREAD_COLOR)

if img is None:
    print("the fils cannot be read")

else:

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("image B&W", img_gray)
    cv2.imwrite("image_GSQL.jpg", img_gray)
    cv2.imshow("input image", img)
    

######### doing the question issue now

    static_matrix = np.zeros_like(img_gray)### creating the static matrix with the same sizes of the image

    ##### using direct assingment (faster and more efficient)
    static_matrix[:] = img_gray

    threshold_min, threshold_max = 100, 255

    ignore , thresholded_matrix = cv2.threshold(static_matrix , threshold_min , threshold_max, cv2.THRESH_BINARY)

    np.savetxt('result.txt', thresholded_matrix, fmt='%d')

    with open ('result.txt', 'r') as file:

        result = file.read()

        print(result)

        cv2.waitKey(0)
        cv2.destroyAllWindows() 