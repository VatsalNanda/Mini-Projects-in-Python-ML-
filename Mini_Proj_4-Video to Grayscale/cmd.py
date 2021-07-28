import os
import sys
import glob
import time
import re
import shutil
from skimage import io
from PIL import Image
from os import listdir,makedirs

from os.path import isfile,join
import matplotlib.pyplot as plt
from tabulate import tabulate
start_time = time.time()
import cv2

arguments = sys.argv
if len(arguments) != 3:
    print("To Execute the script use the following syntax: ")
    print("python <nameoffile>.py indir outdir")
else :

    in_file = arguments[1]
    out_file = arguments[2]

    #os.touch(out_file)
    #files = os.listdir(in_file)
    start_time = time.time()
    #for video in files:
    source_video = cv2.VideoCapture(in_file)
    while True:
        ret,img=source_video.read()
        gray_vid=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        out_file=cv2.imshow("Grayscale video",gray_vid)
        

        dstPath = join(out_file)
        

        cv2.imwrite(dstPath,gray_vid)
    
        

    end_time = time.time()
    print(f"Time Taken to Image to Grayscale", end_time - start_time)

