import numpy as np
import cv2
e1 = cv2.getTickCount()
# hsv_1 = cv2.imread('opencv-logo2.png')
hsv_1 = cv2.imread('wordcup.jpg')

hsv=cv2.cvtColor(hsv_1,cv2.COLOR_BGR2HSV)

red = np.uint8([[[0,0,255 ]]])
hsv_red_high = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)

print(hsv_red_high)
# hsv_red_low =  np.array([110,50,50])
# hsv_red_high = np.array([130,255,255])
hsv_red_low =  np.array([0,100,100])
hsv_red_high = np.array([10,255,255])
mask = cv2.inRange(hsv, hsv_red_low, hsv_red_high)
# cv2.imshow('mask',mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# Bitwise-AND mask and original image
res = cv2.bitwise_and(hsv_1, hsv_1, mask=mask)

cv2.imshow('hsv_1',hsv_1)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
