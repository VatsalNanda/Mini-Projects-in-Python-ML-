import os, sys, time, threading, multiprocessing, shutil

import threading, time, random
from queue import Queue
import os
import string
from matplotlib import pyplot as plt

startTime=time.time()

activeThreads = threading.activeCount()
print("Active Threads = ",activeThreads)

numberOfCores=multiprocessing.cpu_count()
print("Number Of Cores = ",numberOfCores)

startTime=time.time()
inputDirName='input'
outputDirName='output'

# Check inputDirName directory exist or not, we are using the same directory we used in the previous projects of converting text files to uppercase
if os.path.exists(inputDirName) == False:
    print("!! Error: ", inputDirName, " directory doesn't exist")
    exit(0)


# Check outputDirName directory exist or not
try:
    # Delete output directory and then create it
    shutil.rmtree("./%s/"%(outputDirName))
    os.mkdir(outputDirName)
except:
    # Create the output directory
    os.mkdir(outputDirName)


# Function to perform some task - uppercase conversion
def task(fileName):
    inputputFileName="./"+inputDirName+"/"+fileName
    outputFileName="./"+outputDirName+"/"+fileName
    fpr=open(inputputFileName)
    fpw=open(outputFileName,"w")
    
    for line in fpr:
        fpw.write(line.upper())
    fpr.close()
    fpw.close()
    return None

#Creating the threads
def do_stuff(q):
    while not q.empty():
        value = q.get()
        task(value)
        # time.sleep(random.randint(1, 10))
        # print(value)
        q.task_done()
        

# Main Program, converting to uppercase and time taken by the threads in the range of 1-20
print("Program Started....")
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




print(data)

plt.plot(list(data.keys()),list(data.values()))
plt.xlabel("Number of threads")
plt.ylabel("Time Taken")
plt.title("Time taken to convert to 500 text files to Upper Case")
plt.show()
