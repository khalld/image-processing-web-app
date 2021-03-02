from flask import Flask, send_from_directory, send_file, request
import random
import numpy
from PIL import Image
import cv2
import os
from libs.algorithms.mean_or_median import mean_or_median

# da sistemare nella versione finale
# from libs.algorithms.mean import mean
# from libs.algorithms.median import median

from libs.algorithms.bilateral import bilateral_filter

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

@app.route("/median")
def median():
    new_filename = "edited/median.png"

    # ***** non funziona il trycatch! mi prende solo quello sotto l'else, considero solo il file in upload! ******
    # try:
    #     source = getSourceImg(targetUpload, 'uploaded.png')
    # except FileNotFoundError:
    #     print("File not found! Get the default value..!")
    # else:
    # source = getSourceImg(target, 'test.jpg')

    source = getSourceImg(targetUpload, 'uploaded.png')
    img_noisy = Image.open(source).convert("L")
    arr = numpy.array(img_noisy)

    # vecchio
    img_median_applied = Image.fromarray(mean_or_median(arr, len(arr), len(arr[0]), "median"))

    # nuovo da fixare
    # img_median_applied = Image.fromarray( median( arr, len(arr), len(arr[0]) ) )


    saveImg(img_median_applied, target, new_filename)

    return send_image(new_filename)

@app.route("/mean")
def mean():

    new_filename = "edited/mean.png"
    source = getSourceImg(targetUpload, 'uploaded.png')
    img_noisy = Image.open(source).convert("L")
    arr = numpy.array(img_noisy)

    # img_median_applied = Image.fromarray(mean_or_median(arr, len(arr), len(arr[0]), "mean"))

    # nuovo da fixare
    # mean_app = mean(arr, len(arr), len(arr[0]) )

    # vecchio
    mean_app = mean_or_median(arr, len(arr), len(arr[0]), "mean")

    img_mean_app = Image.fromarray(mean_app)

    saveImg(img_mean_app, target, new_filename)

    return send_image(new_filename)

@app.route("/bilateral")
def bilateral():

    new_filename = "edited/bilateral.png"
    source = getSourceImg(targetUpload, 'uploaded.png')

    img_noisy = Image.open(source).convert("L")
    image_bilateral_applied = bilateral_filter(img_noisy, 7,7,6.5)

    saveImg(image_bilateral_applied, target, new_filename)

    return send_image(new_filename)

@app.route("/guided")
def guided():

    print("TODO......")

    return str("OK")

@app.route("/upload", methods=["POST"])
def uploadtest():
    # devo eliminare data:image/jpeg;base64,/ altrimenti non funge..
    data = cleanbase64(request.get_data(as_text='true'))

    imgdata = base64.b64decode(data)
    filename = 'static/images/uploaded/uploaded.png'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)

    return send_from_directory("static/images/uploaded", "uploaded.png")


@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory("static/images", filename)

if __name__ == "__main__":
    app.run(debug=True)
