# Read a video stream from Camera (Frame by Frame)
import cv2

cam = cv2.VideoCapture(0)

while True:

    ret, frame = cam.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if ret == False:
        continue
    
    cv2.imshow("Video Frame", frame)
    cv2.imshow("Gray frame", gray_frame)

    # wait for user input - q to stop the loop
    # key_pressed = cv2.waitKey(1) & 0xFF
    # if key_pressed == ord("q"):
    #     print(key_pressed)
    #     break

    key_pressed = cv2.waitKey(1)
    if key_pressed>0:
        print(key_pressed)
        break

cam.release()
cv2.destroyAllWindows()

