import cv2
import  time


start_time=time.time()
source_vid = cv2.VideoCapture("/Users/vatsalnanda/Desktop/Research Interns and papers/prashant_singh_rana_sir/Mini_Proj_4-Video to Grayscale/COSTA RICA IN 4K 60fps HDR (ULTRA HD).mp4") #input video file


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