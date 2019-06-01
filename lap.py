import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    __, frame =cap.read()
    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    
    edges = cv2.Canny(frame,100,200)
    cv2.imshow('Laplacian',laplacian)
    cv2.imshow('Original',frame)
    cv2.imshow('Edges',edges)
    
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()