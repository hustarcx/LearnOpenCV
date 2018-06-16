import numpy as np
import cv2

#creat a black image
img=np.zeros((512,1024,3),np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(1024,511),(0,120,255),1)

cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

cv2.rectangle(img,(600,0),(630,200),(255,0,0),3)

cv2.circle(img,(510,255),100,(1,100,100),-1)

cv2.ellipse(img,(256,256),(20,50),0,0,360,255,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
print(pts)
pts = pts.reshape((-1,1,2))

print(pts)
cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('my_imag',img)
cv2.waitKey(0)
cv2.destroyAllWindows()