# Mini Project 11- Downloading multiple videos from youtube and sending the zip file to the desired e-mail ID

In this project we ask the user to enter the name of the singer for which we create a mashup. The 'links.txt' file has all the links of the youtube videos to be downloaded, convert them to audio, clip starting 2 minutes, merge audio files, zip it and mail it to the user. 
'download_vids.py'- Used to download the videos from youtube.
'convert_vid_to_audio.py'-Converts the video to audio.
'clip_audio.py'- Clips first 2 minutes of audio files.
'merge_audio.py'-Merges all the audio files into one.
'create_zip.py'- Creates a zip of the above images.
'email_send.py'-Email the zip folder to the desired mail ID.
'command_line_run.png'- Shows us how we run these files in command line.

We ran all the python files in one single file 'email_send.py' after importing their contents in it.

# Installing Dependencies

Important-
Do not pip install pytube3

Use
pip install git+https://github.com/Zeecka/pytube@fix_1060#egg=pytube

pip install moviepy

pip install mutagen

pip install pydub


# Note-
You might run into an error while sending your e-mail through python (only for gmail users) and that might be because you might not have turned on "Less secure app access". Go to this link https://support.google.com/accounts/answer/6010255?hl=en and enable it.

