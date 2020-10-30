import cv2, os
import numpy as np

p1 = cv2.VideoCapture('h3.mp4')

w = int(p1.get(3))
h = int(p1.get(4))
tfs = p1.get(7)

while p1.isOpened() == True:
	for i in range(0,int(tfs)):
		p1.set(1 , i)
		p1_1, p1_2 = p1.read()
		remove_Ch0B = p1_2[:,:,0]
		remove_Ch2R = p1_2[:,:,2]
		d1, mask_1B = cv2.threshold(remove_Ch0B,65,255, cv2.THRESH_BINARY) 
		d3, mask_1R = cv2.threshold(remove_Ch2R,63,255, cv2.THRESH_BINARY)
		mask_1B = cv2.bitwise_not(mask_1B)
		mask_1R = cv2.add(mask_1R,mask_1B)
		mask_1R = cv2.erode(mask_1R,np.ones((8,8)))
		mask_1R = cv2.bitwise_not(mask_1R)
		ol, lv = cv2.findContours(mask_1R,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
		mask_1R = cv2.cvtColor(mask_1R,cv2.COLOR_GRAY2BGR)

		for i2 in range(0,len(ol)):
			cv2.drawContours(mask_1R,ol,i2,(0,0,255),2)
			x, y, w, h = cv2.boundingRect(ol[i2])
			cv2.rectangle(p1_2, (x,y),(x+w,y+h), (255,0,0),2)
			cv2.imshow("p1", p1_2)
			#cv2.waitKey(0)
			if cv2.waitKey(42) != -1:
				os._exit(1)			

	if cv2.waitKey(42) != -1:
		os._exit(1)

p1.release()
cv2.destroyAllWindows()
