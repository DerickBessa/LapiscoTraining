import cv2
import numpy as np

seed = None

def grown_region2( image, seed=None):

    print('Grown function was called...')

    rows , cols = image.shape[:2]
    region = np.zeros_like(image)
    xc , yc = seed

    region[yc , xc] = 255

    directions = [(-1 , -1),(-1 , 0),(-1 , 1),(0 , -1), (0 , 1), (1 , -1), (1 , 0), (1 , 1)]

    growing = True
    while growing:
           growing = False
           for row in range(rows):   ## for one of all pixel in this image...
            for col in range (cols):## ...

                #will make this

                for dx, dy in directions:
                    nx , ny = row + dx , col + dy  # i use the sum, cuz when you sum x + (-1) and y + (-1), for example, u can get the before row and before collum, and this is an 3x3 kernel with 5 diferent directions 
                    
                    if 0 <= nx < image.shape[0] and 0<= ny< image.shape[1]:
                        if image[nx,ny] < 127 and region[nx,ny] == 0 :
                            
                            region[nx,ny] = 255
                            growing = True
    return region
        

def centroid(image):

    
    rows , collums = image.shape[:2]

    xc, yc , count = 0 , 0 , 0

    for row in range(rows):
        for collum in range(collums):
            if image[row, collum] == 255:
                xc += row
                yc += collum
                count += 1

    xm = (xc/count)
    ym = (yc/count)
    
    return xm , ym

def mouse_callback (event , x ,y , flags , param):
    
    global seed

    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'the new seed is setted to ({x} , {y})')
        seed = (x,y)


if __name__ == '__main__':

    img = cv2.imread("image222.jpg", cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscale.jpg", img_gray)

    cv2.namedWindow('Original image', 1)
    cv2.setMouseCallback("Original image", mouse_callback)
    cv2.imshow("Original image", img_gray)


while True:

    
    if cv2.waitKey(1) & 0xFF == ord('c'):
        if seed is not None:

            cv2.imshow("Original image", img_gray)
            grown_image = grown_region2(img_gray , seed)
            xc , yc = centroid(grown_image)

            new_img = cv2.cvtColor(grown_image, cv2.COLOR_GRAY2BGR)
            new_img[np.where(grown_image == 255)] = [255, 0 , 0]

            cv2.circle(new_img, (int(yc) ,int(xc)), 5 , (0 , 255, 0), -1)


            cv2.imshow(' ', seed)
            cv2.imshow('Segmented Centroided image' ,new_img)
            
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            continue
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            print("Closing all windows..")
            break
cv2.destroyAllWindows()
