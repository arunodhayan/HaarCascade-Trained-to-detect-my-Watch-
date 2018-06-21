import cv2
import numpy as np
watch_cascade = cv2.CascadeClassifier('w_cascade.xml')
cap = cv2.VideoCapture(1)  # videocapture(1) means second webcam is connected and o means 1st webcam is connected

while True:
    ret , img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    watches = watch_cascade.detectMultiScale(gray)
    for (x,y,w,h) in watches:
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,'watch',(x-w,y-h),font,0.5,(0,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    cv2.imshow('img',img)
     

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
