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

    in_directory = arguments[1]
    out_directory = arguments[2]

    os.mkdir(out_directory)
    files = os.listdir(in_directory)
    start_time = time.time()
    for image in files:
        img = cv2.imread(os.path.join(in_directory,image))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        dstPath = join(out_directory,image)
        

        cv2.imwrite(dstPath,gray)
    
        

    end_time = time.time()
    print(f"Time Taken to Image to Grayscale", end_time - start_time)

