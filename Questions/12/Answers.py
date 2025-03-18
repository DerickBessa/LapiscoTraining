import cv2
import numpy as np

data = np.loadtxt('RESULT.txt')
image = np.uint8(data)
cv2.imshow(" from txt to BGR" , image)
cv2.imwrite("from_txt2bgr.jpg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()