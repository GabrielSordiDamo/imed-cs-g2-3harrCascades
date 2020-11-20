import cv2


cascade = cv2.CascadeClassifier('./cascade/cascade.xml')
video = cv2.VideoCapture(0)

while True:
    flag, frame = video.read()

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    itemToFind = cascade.detectMultiScale(frame, 1.2, 5)

    for (x, y, w, h) in itemToFind:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow('video', frame)
    key = cv2.waitKey(5)
    if key == 27:
        break

cv2.destroyAllWindows()
