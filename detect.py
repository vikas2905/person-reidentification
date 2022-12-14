import cv2
import numpy as np
from evaluator import get_acc_score
import os
flag=0
list_dr = '/Users/vikas/Human-detection-and-Tracking/results'
for image in os.listdir(list_dr):
	if(image.endswith(".jpg")):
		input_path = os.path.join(list_dr, image)
		a = cv2.imread(input_path)
		am = cv2.resize(a,(50,50))
		b = cv2.imread("2091.jpg")
		bm = cv2.resize(b,(50,50))
		difference = cv2.subtract(am, bm)
		result = not np.any(difference)
		if result is True:
    			print("Person Found")
    			flag = 1
    			get_acc_score(flag)
    			break
if flag==0:
	print("person not found ")
	get_acc_score(flag)
