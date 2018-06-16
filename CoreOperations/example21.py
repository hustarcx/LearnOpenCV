import numpy as np
import cv2
e1 = cv2.getTickCount()
img1 = cv2.imread('wordcup.jpg')
img2 = cv2.imread('logo.jpg')
print(img1.shape)
print(img2.shape)
rows,cols,channels = img2.shape

roi = img1[0:rows, 0:cols]
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print(time)
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('img2grap',img2gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

