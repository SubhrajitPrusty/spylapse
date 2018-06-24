from cv2 import *
import time
import os

def takePicture(index):
	cam = VideoCapture(0)
	s, img = cam.read()
	if s:
		imwrite(os.path.join("img","t-{}.jpg".format(index)),img)

while(True):
	takePicture(int(time.time()))
	time.sleep(2)
