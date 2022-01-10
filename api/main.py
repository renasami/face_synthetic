from fastapi import FastAPI
import base64 
import cv2
import numpy as np
import random
import datetime
import os
import facemorpher
import glob
import binascii

app = FastAPI()

@app.get("/")
def root():
    return {"message":"world"}


def generate_syntheticed_faces(files:list,folder) -> base64:
    output = "{}/result.png".format(folder)
    facemorpher.averager(files,background='transparent',out_filename=output,plot=False)
    img = open(output, "rb")
    return base64.b64encode(img.read())



@app.post("/img_save")
def save_img(imgs):
    print(type(imgs))
    imgs = eval(imgs)
    if len(imgs) == 0:
        return False
    date = datetime.datetime.now().strftime("%Y%m%d%H%M")
    rand = random.random()
    img_folder = "tmp/{}{}".format(date,rand)
    os.mkdir(img_folder)
    for i,img in enumerate(imgs):
        image_file="./{}/{}.png".format(img_folder,i)
        binary = base64.b64decode(img)
        # f = open(image_file,"bw")
        # f.write(binary)
        # f.close()
        
        with open(image_file, 'bw') as f4:
            f4.write(binary)        
        files = ["{}/{}.png".format(img_folder,n) for n in range(2)]
    result = generate_syntheticed_faces(files,img_folder)

    return result.decode("utf-8")

