import shutil
import os
import time
from matplotlib import pyplot as plt
from queue import Queue
import threading
import cv2


# Function to Convert the Videos to Gray Scale

def task(video_path):
    video = cv2.VideoCapture(f'./input/{video_path}')
    while True:
        ret, frame = video.read()
        if ret:
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow('temp',gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else :
            break

    video.release()

   
# Function to send task to threads
def do_stuff(q):
    while not q.empty():
        value = q.get()
        task(value)
        q.task_done()



 


# Convert Videos to Gray Scale and note the time taken
data = {}

for t in range(1,21):
    jobs = Queue()
    for elem in os.listdir('input'):
        jobs.put(elem)
    start = time.time()
    for i in range(t):
        worker = threading.Thread(target=do_stuff, args=(jobs,))
        worker.start()
    
    jobs.join()
    end = time.time()
    print(t, end - start)
    data[t] = end - start


#  Plot the required Data
print(data)

plt.plot(list(data.keys()),list(data.values()))
plt.xlabel("Number of threads")
plt.ylabel("Time Taken")
plt.title("Time taken to convert 100 Images from color to gray Scale")
plt.show()
