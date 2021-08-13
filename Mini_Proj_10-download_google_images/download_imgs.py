from google_images_download import google_images_download

element=input('Enter the keyword')
lim=input('Enter the number of images you want to download(maximum 100)')

#instantiate the class
response = google_images_download.googleimagesdownload()
arguments = {"keywords":element,
             "limit":lim,"print_urls":False}
paths = response.download(arguments)

#print complete paths to the downloaded images
print(paths)
