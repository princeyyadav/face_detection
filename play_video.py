import cv2 as cv

cap = cv.VideoCapture("videoplayback.mp4")
wret = cap.set(cv.CAP_PROP_FRAME_WIDTH, 500)
hret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 500)
print(wret, hret) # returned false

w, h = cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT)
print(w, h)

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

# define codec
fourcc = cv.VideoWriter_fourcc(*'XVID')

# video writer object
out = cv.VideoWriter('output.avi', fourcc, 20.0, (int(w),int(h))) 

while True:

    ret, frame = cap.read()
    # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    if not ret:
        print("Frame not captured")
        break

    face_rects = face_cascade.detectMultiScale(frame, 1.5, 4)
    for x, y, w, h in face_rects:
        cv.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    # write the file having detected faces
    out.write(frame)

    cv.imshow("Avengers", frame)

    key_pressed = cv.waitKey(1)
    if key_pressed == ord("q"):
        print("Q pressed. Exit..")
        break

cap.release()
cv.destroyAllWindows()
