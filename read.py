import numpy as np
import cv2
import os

file_name = os.path.join('data', 'train.mp4')
file_test = os.path.join('data', 'test.mp4')
cap = cv2.VideoCapture(file_test)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
