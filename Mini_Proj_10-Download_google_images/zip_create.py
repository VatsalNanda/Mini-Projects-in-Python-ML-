import zipfile
import os
from resize import resized_dir
folder_to_be_zipped = resized_dir
filename=input('Enter the filename fir zip')
with zipfile.ZipFile(filename+'.zip', 'w', zipfile.ZIP_DEFLATED) as newzip:
    for dirpath, dirnames, files in os.walk(folder_to_be_zipped):
        for file in files:
            newzip.write(os.path.join(dirpath, file))
