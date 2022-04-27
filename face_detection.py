# Install OpenCV using
# pip install opencv-python

import cv2

a = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
b = cv2.VideoCapture(0)

while True:
    c_rec, d_image = b.read()
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
    f = a.detectMultiScale(e, 1.3, 6)

    for (x, y, w, h) in f:
        cv2.rectangle(d_image, (x, y), (x+w, y+h), (255,0,0), 5)

    cv2.imshow('img', d_image)
    if cv2.waitKey(1) & 0xFF == 27:
        break 

b.release()
cv2.destroyAllWindows()




