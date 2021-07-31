import os
import sys
import time
import shutil
import cv2
start_time = time.time()


arguments = sys.argv
if len(arguments) != 2:
    print("To Execute the script use the following syntax: ")
    print("python <nameoffile>.py infile")
else :

    in_file = arguments[1]
    
    source_vid=cv2.VideoCapture(in_file)
    
    while True:


        ret, img = source_vid.read() # extracting the frames


        gray_vid = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converting to gray-scale



        cv2.imshow("Gray video", gray_vid) # displaying the video




    # exiting the loop
        time_var = time.time() - start_time
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

print("The time taken to convert the video to grayscale is", time_var, "seconds")
# closing the window
cv2.destroyAllWindows()
source_vid.release()
  
    
        

    
