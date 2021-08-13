from pytube import YouTube
from pytube.streams import Stream

SAVE_PATH='/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/Youtube_video_downloader/Youtube downloads'

link=open('links.txt','r') 
for i in link: 
    try: 
          
        # object creation using YouTube
        # which was imported in the beginning 
        yt = YouTube(i) 
    except: 
          
        #to handle exception
        print("Connection Error")  
      
    #filters out all the files with "mp4" extension 
    #mp4files = yt.filter('mp4') 
      
    # get the video with the extension and
    # resolution passed in the get() function 
    stream = yt.streams.first()
    stream.download(SAVE_PATH) 
