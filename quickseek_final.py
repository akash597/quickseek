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
    return int(total_seconds)
    

key = input("ENTER THE KEY PHRASE :")
file = open('tcs.srt','r')

previousLine = ""

for line in file.readlines():
    if key in line:
        t = return_seconds(previousLine)
        break;
    previousLine = line


cap = cv2.VideoCapture('tcs.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)
count = 0
success = True
while success:
    success,frame = cap.read()
    count+=1
    ts = count/fps
    if t == ts:
      print("time stamp of current frame:",count/fps)
      print("this will take some time.......")
      print("Press Q to quit")
      f_count = count
cap.set(cv2.CAP_PROP_POS_FRAMES, f_count)
# Check if camera opened successfully 
if (cap.isOpened()== False):  
  print("Error opening video  file") 
   
# Read until video is completed 
while(cap.isOpened()): 
      
  # Capture frame-by-frame 
  ret, frame = cap.read() 
  if ret == True: 
   
    # Display the resulting frame 
    cv2.imshow('Frame', frame) 
   
    # Press Q on keyboard to  exit 
    if cv2.waitKey(25) & 0xFF == ord('q'): 
      break
   
  # Break the loop 
  else:  
    break
   
# When everything done, release  
# the video capture object 
cap.release() 
   
# Closes all the frames 
cv2.destroyAllWindows() 
