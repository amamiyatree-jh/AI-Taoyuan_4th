import cv2
import numpy as np

pic01 = cv2.imread("h2.png", -1)
m1 = np.full(pic01.shape,(0,255,0),np.uint8)
bu = cv2.multiply(pic01,m1)
m2 = np.full(pic01.shape,(255,0,255),np.uint8)
bu = cv2.add(bu,m2)
pic02 = cv2.cvtColor(bu , cv2.COLOR_BGR2GRAY)
cv2.imshow("p2", pic02)

cv2.waitKey(0)
cv2.destroyAllWindows()
