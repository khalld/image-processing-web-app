from flask import Flask, send_from_directory, send_file, request
import random
import numpy
from PIL import Image
import cv2
import os
from libs.algorithms.remove_noise import remove_noise
from libs.algorithms.bilateral import bilateral_filter
from bunch import bunchify

from libs.utils import saveImg, getSourceImg, cleanbase64

import base64
import io

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

target = os.path.join(APP_ROOT, 'static/images')

targetUpload = os.path.join(APP_ROOT, 'static/images/uploaded')


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/median", methods=["POST"])
def median():

    req = request.get_json() # dict type

    new_filename = "edited/median.png"
    input_img = Image.open(getSourceImg(targetUpload, 'uploaded.png'))
    result = remove_noise(input_img,req['kernel_dim'],"median")
    saveImg(result, target, new_filename)

    return send_image(new_filename)

@app.route("/mean", methods=["POST"])
def mean():

    req = request.get_json()

    new_filename = "edited/mean.png"
    input_img = Image.open(getSourceImg(targetUpload, 'uploaded.png'))
    result = remove_noise(input_img,req['kernel_dim'],"mean")
    saveImg(result, target, new_filename)

    return send_image(new_filename)

@app.route("/bilateral", methods=["POST"])
def bilateral():

    req = request.get_json()

    radius = req['radius']
    sigma_d = req['sigma_d']
    sigma_r = req['sigma_r']

    new_filename = "edited/bilateral.png"
    input_img = Image.open(getSourceImg(targetUpload, 'uploaded.png'))
    result = bilateral_filter(input_img, radius, sigma_d, sigma_r)
    saveImg(result, target, new_filename)

    return send_image(new_filename)

@app.route("/guided")
def guided():

    print("TODO......")

    return str("OK")

@app.route("/upload", methods=["POST"])
def uploadtest():
    # print("**** REQUEST****\n", receved['image'])
    # devo eliminare data:image/jpeg;base64,/ altrimenti non funge..

    # vecchio .. # funziona solo con jpeg..

    data = cleanbase64(request.get_data(as_text='true'))
    imgdata = base64.b64decode(data)

    # nuovo ...

    # receved = request.get_json()
    # imgdata = receved['image']

    # print(type(imgdata))

    filename = 'static/images/uploaded/uploaded.png'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)

    return send_from_directory("static/images/uploaded", "uploaded.png")


@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory("static/images", filename)

if __name__ == "__main__":
    app.run(debug=True)
