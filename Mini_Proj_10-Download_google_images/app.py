import numpy as np
from flask import Flask,request,jsonify,render_template

from download_imgs import download_images
from email_send import mail_user

app=Flask(__name__)


@app.route("/",methods=["GET","POST"])

def main_page():
    if request.method == "POST":
        element = request.form['element'].replace(' ','').lower()
        email_id = request.form['email_id']
        lim = int(request.form['lim'])
        download_images(element,lim)
        mail_user(email_id)
        # print(keyword,emailid,limit)
    return render_template("index_new.html")


if __name__=="__main__":
    app.run(debug=True)
