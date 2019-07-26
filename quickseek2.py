import cv2
import numpy as np
import re

key = input("ENTER THE KEY PHRASE")
file = open('tcs.srt','r')

for line in file.readlines():
	if re.search(r'^%s'%key, line, re.I):
		print(line)
