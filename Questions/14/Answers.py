import cv2
import numpy as np

frame_count = 0

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("error in camera acess")
    exit()


while True:
    #### frame capture

    ret, frame = cap.read()

    gray_scale_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    if not ret:

        print("error in frame capture")
        break

    else:
        
        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            
            filename = f"frame_capture_{frame_count}.jpg"
            cv2.imwrite(filename, gray_scale_frame)
            print(f"Frame {frame_count} saved!!")
            
            frame_count += 1 

        elif cv2.waitKey(1) & 0xFF == ord('q'):
            print("Stoping capture..")
            break

cap.release()
cv2.destroyAllWindows()
