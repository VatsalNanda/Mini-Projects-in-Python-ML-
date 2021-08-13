import os
import glob
import time
import re
import shutil
from os import listdir, makedirs
from os.path import isfile, join
import matplotlib.pyplot as plt
from tabulate import tabulate
from download_imgs import element

start_time = time.time()
import cv2


path = '/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/download_google_images/downloads/'+element # Source Folder


outputDirName=input('Enter your output directory name where you want the grayscale image to be stored')

try:
    # Delete output directory and then create it
    shutil.rmtree("./%s/"%(outputDirName))
    os.mkdir(outputDirName)
except:
    # Create the output directory
    os.mkdir(outputDirName)
dstpath ='/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/download_google_images/'+outputDirName  # Destination Folder

files = [f for f in listdir(path) if isfile(join(path, f))]
x = len(os.listdir(dstpath))

for image in files:
    try:

        img = cv2.imread(os.path.join(path, image))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        dstPath = join(dstpath, image)

        cv2.imwrite(dstPath, gray)

        
    except:
        print("{} is not converted".format(image))

time1 = time.time() - start_time
print("time1k=",time1,"s")
