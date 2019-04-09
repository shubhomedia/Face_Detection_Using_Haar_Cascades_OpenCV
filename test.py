import numpy as np
import cv2

img = cv2.imread("test.jpg",1)
img_1 = cv2.imread("test",0)

print(img)
print(type(img))

resize_my_image = cv2.resize(img,(500,500))
cv2.imshow("resize",resize_my_image)
cv2.waitKey(0)
cv2.destroyAllWindows()