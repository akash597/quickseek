import cv2
import numpy as np

cap = cv2.VideoCapture('tcs.mp4')




def choice():
    print("\n~~~KEY NOTES~~~\n1.Rajesh's initial comments\n2.50 Year Milestone\n3.Querter DETAILS\n4.Profitability\n5.Cash conversion and Cash Balance\n0.QUIT")
    ch = input("ENTER YOUR CHOICE-")
    s = True
    while s:
            if ch == "1":
            		t = 58
            		return t
            elif ch == "2":
            		t = 246
            		return t
            elif ch == "3":
            		t = 268
            		return t;
            elif ch == "4":
            		t = 388
            		return t
            elif ch == "5":
            		t = 442
            		return t
            else:
            	print("Invalid choice, please choose again")
            	print("\n")





fps = cap.get(cv2.CAP_PROP_FPS)
count = 0
success = True
timestamp = choice()
while success:
    success,frame = cap.read()
    count+=1
    ts = count/fps
    if timestamp == ts:
      print("time stamp current frame:",count/fps)
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
