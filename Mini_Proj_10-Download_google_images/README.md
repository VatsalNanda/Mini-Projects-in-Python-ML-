# Mini Project 10- Downloading multiple images from google and sending the zip file to the desired e-mail ID

In this project we ask the user to enter the name of the element for which they want the images and ask the number of images they want. Then we convert these images to grayscale, resize them to 50%, zip them in a file and send the zip file to the desired mail ID.
'download_imgs.py'- Used to download the images from google
'grayscale.py'-Converts the downloaded images to grayscale
'resize.py'- Resize the grayscale images to 50% of their original size.
'zip_create.py'- Creates a zip of the above images.
'email_send.py'-Email the zip folder to the desired mail ID.
'command_line_run.png'- Shows us how we run these files in command line.

We ran all the python files in one single file 'email_send.py' after importing their contents in it. We ran this on the local host using **Flask**.

# Installing Dependencies

Important-
Do not pip install google_images_download

Use
pip install git+https://github.com/Joeclinton1/google-images-download

pip install flask

# Note-
You might run into an error while sending your e-mail through python (only for gmail users) and that might be because you might not have turned on "Less secure app access". Go to this link https://support.google.com/accounts/answer/6010255?hl=en and enable it.

# Command line run 

<img width="677" src="https://github.com/VatsalNanda/Mini-Projects-in-Python-ML-/blob/main/Mini_Proj_10-Download_google_images/command_line_run.png">

# Web page Preview

<img width="677" src="https://github.com/VatsalNanda/Mini-Projects-in-Python-ML-/blob/main/Mini_Proj_10-Download_google_images/web_page.png">
