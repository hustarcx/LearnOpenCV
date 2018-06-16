import  numpy as np
import  cv2
img=cv2.imread('wordcup.jpg')
px=img[100,100]
print(px)
blue=img[100,100,0]
print(blue)
img[100,100]=[255,255,0]
print(img[100,100])
print(img.shape)
print(img.size)
print(img.dtype)
#cv2.rectangle(img,(180,470),(270,560),(0,255,0),1)
ball=img[470:560,180:270]
img[470:560,580:670]=ball

b,g,r = cv2.split(img)
print(b)
print(b.shape)
img[:,:,2] = 255
#img[:,:,0] = 255
#img[:,:,1] = 255
cv2.imshow('my_wordcup',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
