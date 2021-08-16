from google_images_download import google_images_download
import os
import glob
import time
import re
import shutil
from os import listdir, makedirs
from os.path import isfile, join
import matplotlib.pyplot as plt
from tabulate import tabulate
from PIL import Image
import glob
import os
import zipfile

#from download_imgs import element

#start_time = time.time()
import cv2
#element=input('Enter the keyword')
#lim=input('Enter the number of images you want to download(maximum 100)')

#instantiate the class
def download_images(element,lim):
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":element,
                 "limit":lim,"print_urls":False}
    paths = response.download(arguments)

    #print complete paths to the downloaded images
    print(paths)
    
    path = '/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/Mini_Proj_10-Download_google_images/downloads/'+element # Source Folder


#outputDirName=input('Enter your output directory name where you want the grayscale image to be stored')

    try:
        # Delete output directory and then create it
        shutil.rmtree("./%s/"%('gray'))
        os.mkdir('gray')
    except:
        # Create the output directory
        os.mkdir('gray')
    dstpath ='/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/Mini_Proj_10-Download_google_images/gray'  # Destination Folder

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
            
    image_list=[]
    resized_images=[]
    for filename in glob.glob('/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/Mini_Proj_10-Download_google_images/gray/*'):
        print(filename)
        img=Image.open(filename)
        #print('size:{}'.format(image.size))
        image_list.append(img)



    #print(resized_images)
    for image in image_list:
        #image.show()
        width, height = image.size
        
    #     print(width)
    #     print(height)
    #     print(int(width/2))
    #     print(int(height/2))
        image=image.resize((int(width/2),int(height/2)))
        #print(image)
        resized_images.append(image)
        #print(len(resized_images))

    #resized_dir=input('Enter the name of the resized folder')
    try:
        # Delete output directory and then create it
        shutil.rmtree("./%s/"%('resized_dir'))
        os.mkdir('resized_dir')
    except:
        # Create the output directory
        os.mkdir('resized_dir')


    for (i,new) in enumerate(resized_images):
         new.save(f'/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/Mini_Proj_10-Download_google_images/resized_dir/img'+str(i)+'.jpg')

    image_list.clear()
    
    #folder_to_be_zipped = resized_dir
    
    with zipfile.ZipFile('image_gray_and_resized.zip', 'w', zipfile.ZIP_DEFLATED) as newzip:
        for dirpath, dirnames, files in os.walk('resized_dir'):
            for file in files:
                newzip.write(os.path.join(dirpath, file))

            
    
    
    
    
