from cv2 import *
import time
import os

def takePicture(index):
	cam = VideoCapture(0)
	s, img = cam.read()
	if s:
		imwrite(os.path.join("img","t-{}.jpg".format(index)),img)
i = 1
while(True):
	# takePicture(int(time.time()))
	# not using because glob (*) is not supported on Windows ffmpeg
	takePicture(i)
	i+=1
	time.sleep(2)
