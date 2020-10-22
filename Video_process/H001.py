import cv2
import numpy as np
s_X = 0
s_Y = 100

T_S = 8
while True:
	i = 0
	while i < 300:
		i += 1
		#print(i, end = '')
		p1 = np.full((300, 700, 3), (214,140,84), np.uint8)
		cv2.rectangle(p1, (s_X*(i-1),s_Y), (s_X*(i-1)+100,s_Y+100 ), (0,0,255), -1)
		cv2.imshow('p1',p1)
		cv2.waitKey(T_S)
		s_X = 2
		if cv2.waitKey(1) != -1:
			os._exit()		

	i = 299
	while i > 1:
		i -= 1
		#print(i, end = '')
		p1 = np.full((300, 700, 3), (214,140,84), np.uint8)
		cv2.rectangle(p1, (s_X*(i-1),s_Y), (s_X*(i-1)+100,s_Y+100 ), (0,0,255), -1)
		cv2.imshow('p1',p1)
		cv2.waitKey(T_S)
		s_X = 2
		if cv2.waitKey(1 ) != -1:
			os._exit()
