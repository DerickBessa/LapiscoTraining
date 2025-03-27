import cv2
import numpy as np

frame_count = 0

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("error to open Camera")
    exit()

while True:

    # capture the frame

    ret , frame = cap.read()

    gray_scale_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    gray_scale_frame_canny = cv2.Canny(gray_scale_frame, threshold1 = 10 , threshold2= 100)

    cv2.imshow("Video", gray_scale_frame_canny)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        filename = f"frame_capture_{frame_count}.jpg"
        cv2.imwrite(filename, gray_scale_frame_canny)
        print(f"Frame{frame_count + 1} saved!!")

        frame_count += 1
    
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        print("Stoping capture..")
        break

cap.release()
cv2.destroyAllWindows()