import cv2
import numpy as np

img = cv2.imread("../1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5),np.float32)/25
gray = cv2.filter2D(gray,-1,kernel)
edges = cv2.Canny(gray,400,600,apertureSize = 5)
cv2.imshow('image',edges)
cv2.waitKey(0)

lines = cv2.HoughLines(edges,1,np.pi/180,15)
for i in range(8):
    for rho,theta in lines[i]:
           a = np.cos(theta)
           b = np.sin(theta)
           x0 = a*rho
           y0 = b*rho
           x1 = int(x0 + 1000*(-b))
           y1 = int(y0 + 1000*(a))
           x2 = int(x0 - 1000*(-b))
           y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('image',img)
cv2.waitKey(0)