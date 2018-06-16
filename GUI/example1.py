import  numpy as np
import  cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('sea.jpg',1)
cv2.imshow('my_sea',img)
cv2.imwrite('my_sea1.jpeg',img)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

# cv2.destroyWindow('my_sea')
# k = cv2.waitKey(0)
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'): # wait for 's' key to save and exit
#     cv2.imwrite('my_sea2.png',img)
#     cv2.destroyAllWindows()
#cv2.destroyAllWindows()
