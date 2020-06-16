import cv2
import os

files = os.listdir('./')
files = filter(lambda x: x.endswith('.png'), files)
for f in files:
	print(f)
	img = cv2.imread(f)
	cv2.imwrite(f.split('.')[0] + '.jpg', img)