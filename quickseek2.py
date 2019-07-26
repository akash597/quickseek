import cv2
import numpy as np
import re

def return_seconds(line):
    timeValues = line[:line.index("-->")].strip().replace(",",":").split(":")
    timeValues = list(map(int, timeValues))
    hours_to_seconds = timeValues[0] * 3600
    minutes_to_seconds = timeValues[1] * 60
    seconds = timeValues[2]
    milliseconds_to_seconds = round(timeValues[3]/1000, 2)
    total_seconds = hours_to_seconds + minutes_to_seconds + seconds + milliseconds_to_seconds
    return total_seconds

key = input("ENTER THE KEY PHRASE")
file = open('tcs.srt','r')

previousLine = ""

for line in file.readlines():
    if key in line:
        print("Starting seconds at line is {}".format(return_seconds(previousLine)))
    previousLine = line

