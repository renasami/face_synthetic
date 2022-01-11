from fastapi import FastAPI
import base64 
import cv2
from fastapi.params import Body
import numpy as np
import random
import datetime
import os
import facemorpher
import glob
import binascii
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.responses import JSONResponse

app = FastAPI()
origins = [
    "http://localhost:8080",
]

app.add_middleware(GZipMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {"message":"world"}

@app.post("/test")
def test(body=Body(...)):
    print(body)
    # imgs = eval(body)
    # print(imgs)
    new = ""
    # print(imgs)
    for n in body:
        print(n["foo"])
        print(base64.b64decode(n["foo"]).decode("utf-8"))
        new += str(base64.b64decode(n["foo"]).decode("utf-8"))
    print(new)
    return JSONResponse({"mes": "hello"})

@app.get("/test")
def tests():
    return JSONResponse({"mes": "hello"})

def generate_syntheticed_faces(files:list,folder) -> base64:
    output = "{}/result.png".format(folder)
    facemorpher.averager(files,background='transparent',out_filename=output,plot=False)
    img = open(output, "rb")
    return base64.b64encode(img.read())


@app.post("/img_save")
def save_img(body=Body(...)):
    if len(body) == 0:
        return False
    date = datetime.datetime.now().strftime("%Y%m%d%H%M")
    rand = random.random()
    img_folder = "tmp/{}{}".format(date,rand)
    os.mkdir(img_folder)
    for i,img in enumerate(body):
        image_file="./{}/{}.png".format(img_folder,i)
        binary = base64.b64decode(img)
        with open(image_file, 'bw') as f4:
            f4.write(binary)        
        files = ["{}/{}.png".format(img_folder,n) for n in range(2)]
    result = generate_syntheticed_faces(files,img_folder)

    return "data:image/png;base64," + str(result.decode("utf-8"))

