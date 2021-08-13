from PIL import Image
import glob
import os
from grayscale import outputDirName
image_list=[]
resized_images=[]
for filename in glob.glob('/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/download_google_images/'+outputDirName+'/*'):
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

resized_dir=input('Enter the name of the resized folder')
try:
    # Delete output directory and then create it
    shutil.rmtree("./%s/"%(resized_dir))
    os.mkdir(resized_dir)
except:
    # Create the output directory
    os.mkdir(resized_dir)


for (i,new) in enumerate(resized_images):
     new.save(f'/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/download_google_images/'+resized_dir+'/img'+str(i)+'.jpg')

image_list.clear()
