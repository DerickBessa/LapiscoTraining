import cv2
import numpy as np


img = cv2.imread("img11.jpg", cv2.IMREAD_COLOR)

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

    rows, collums = static_matrix.shape

    xc = 0
    yc = 0
    count = 0

    for row in range(rows):
        for collum in range(collums):
            if static_matrix[row , collum] == 0:
                xc += row
                yc += collum
                count += 1

    xc_media = int (xc/count)
    yc_media = int (yc/count)

    centroid = (xc_media, yc_media)
    radius = 5
    
    static_matrix = cv2.cvtColor(static_matrix, cv2.COLOR_GRAY2BGR)

    centroid_img = cv2.circle(static_matrix , centroid , 10, [0 , 0 , 255], -1 )

    cv2.imshow(" image with red centroid", centroid_img)
    cv2.imwrite("red_centroid.jpg", centroid_img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows
