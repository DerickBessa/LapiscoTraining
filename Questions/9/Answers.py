import cv2
import numpy as np

img = cv2.imread("imagem9.jpg", cv2.IMREAD_COLOR)

if img is None:
    print("the fils cannot be read")

else:

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("image B&W", img_gray)
    cv2.imwrite("image_GSQL.jpg", img_gray)
    cv2.imshow("input image", img)
    

######### doing the question issue now

    static_matrix = np.zeros_like(img)### creating the static matrix with the same sizes of the image

    #### now i can use the FOR form, look:
    #
    #    for i in range(img.shape[0]):     #rows
    #       for j in range(img.shape[1]):  #collums
    #      static_matrix[i , j] = img[i ,j]
    #
    ##### using direct assingment (faster and more efficient)
    static_matrix[:] = img  ##direct attribution

    np.savetxt('static_matrix.txt' , static_matrix.reshape(-1, 3), fmt='%d')


    with open ('static_matrix.txt', 'r') as file:

        content = file.read()

        print("R  G  B")
        print(content)

cv2.waitKey(0)
cv2.destroyAllWindows()