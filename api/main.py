from fastapi import FastAPI
import base64 
import cv2
import numpy as np
import random

app = FastAPI()

@app.get("/")
def root():
    return {"message":"world"}

print(cv2.__version__)

@app.post("/img_save")
def save_img(imgs):

    rand = random.random()
    image_file='{}decode.png'.format(rand)
    binary = base64.b64decode(imgs)
    with open(image_file, 'bw') as f4:
        f4.write(binary)
    # return binary
