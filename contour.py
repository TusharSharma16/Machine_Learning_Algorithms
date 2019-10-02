import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io


im = cv2.imread('../1.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

# Contoured image
ret,thresh = cv2.threshold(imgray, 120,255,cv2.THRESH_BINARY)
contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
for contour in contours:
   cv2.drawContours(im, contour, -1, (0, 255, 0), 3)
cv2.imshow("contour",im)
cv2.waitKey(0)