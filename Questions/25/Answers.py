import cv2
import numpy as np

seed = (0, 0)

image = cv2.imread("image.jpg")

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

mask = np.zeros_like(grayscale_image)

event_count = 0

def grown_region(image, image_marked ,  seed=None):
    rows, collums = image.shape[:2]  # get the shape of the  image
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    current_found = 0
    previous_points = 1  # set the previous points to 1, so it will enter the while loop
    while previous_points != current_found:
        previous_points = current_found
        current_found = 0

        for row in range(rows):
            for col in range(collums):
                if image_marked[row, col] == 1:
                    for (dx , dy) in directions:
                        nx , ny = row + dx , col + dy
                        if 0 <= nx < rows and 0 <= ny < collums:
                                if image[nx,ny] < 230 :
                                    image_marked[nx,ny] = 1
                                    current_found += 1
                elif image_marked[row, col] == 2:
                    for (dx , dy) in directions:
                        nx , ny = row + dx , col + dy
                        if 0 <= nx < rows and 0 <= ny < collums:
                                if image[nx,ny] < 230 :
                                    image_marked[nx,ny] = 2
                                    current_found += 1
                elif image_marked[row, col] == 3:
                    for (dx , dy) in directions:
                        nx , ny = row + dx , col + dy
                        if 0 <= nx < rows and 0 <= ny < collums:
                                if image[nx,ny] < 230 :
                                    image_marked[nx,ny] = 3
                                    current_found += 1
    return image_marked

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed
        global event_count
        global mask
        
        print(f'The new seed is set to ({x}, {y})')
        event_count += 1
        if event_count %3 == 1:
            event_count = 1
            mask[np.where(mask == 1)] = 0
        if event_count %3 == 2:
            event_count = 2
            mask[np.where(mask == 2)] = 0
        if event_count %3 == 0:
            event_count = 3
            mask[np.where(mask == 3)] = 0
        mask[y, x] = event_count  ##marking the seed point in the image
        
if __name__ == '__main__':
    
    cv2.namedWindow('Marked Object', 1)
    cv2.imshow('Marked Object', grayscale_image)
    cv2.setMouseCallback('Marked Object', mouse_event)

    cv2.waitKey(0)
    segmented_image = grown_region(grayscale_image, mask, seed)
    rows,cols = segmented_image.shape[:2]
    new_image = np.zeros([rows,cols,3 ], np.uint8)
    new_image[np.where(segmented_image == 1)] = [0, 0, 255]
    new_image[np.where(segmented_image == 2)] = [255, 0, 0]
    new_image[np.where(segmented_image == 3)] = [0, 255, 0]
    
    cv2.imshow("Segmented image", new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 