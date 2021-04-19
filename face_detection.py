import cv2

cam = cv2.VideoCapture(index=0) # video capture object
if not cam.isOpened():
    print("Camera not opened")
    exit()
wret = cam.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
hret = cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

print(wret, hret)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # pretrained model to detect faces

while True:

    ret, frame = cam.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert into grarscale img

    if not ret:
        print("Can't receive frame")
        break

    # detect faces in the image
    faces_rect = face_cascade.detectMultiScale(frame, 1.3, 5)
    
    # show these rect on the image
    for x, y, w, h in faces_rect:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

    cv2.imshow("Video Frame", frame)

    # exit loop if any key is pressed
    key_pressed = cv2.waitKey(1)
    if key_pressed > 0:
        print(chr(key_pressed), key_pressed)
        break

cam.release()
cv2.destroyAllWindows()



    

