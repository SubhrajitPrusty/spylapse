from cv2 import *
import time
import os

def takePicture(index):
	cam = VideoCapture(0)
	s, img = cam.read()
	if s:
		imwrite(os.path.join("img","t-{}.jpg".format(index)),img)
i = 1

try:
	print("Ctrl+c to stop recording and start stitching the images...")
	while(True):
		# takePicture(int(time.time()))
		# not using because glob (*) is not supported on Windows ffmpeg
		takePicture(i)
		i+=1
		time.sleep(2)
except:
	pass
finally:
	print("Stitching together...")
	os.system("ffmpeg -r 12 -i img/t-%d.jpg -c:v libx264 -y {}.mp4".format(time.strftime("%d-%m-%y.%I-%M")))
	os.chdir("img")
	for files in os.listdir("."):
            if not files.startswith("."):
                os.remove(files)
