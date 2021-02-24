from flask import Flask, send_from_directory, send_file
import random
import numpy
from PIL import Image
import cv2
import os
from algorithm.median import mean_or_median

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Metodo che salva un'immagine (img) nel target fornito con il nome di new_filename
def saveImg(img, target, new_filename):
    destination = "/".join([target, new_filename])
    if os.path.isfile(destination):
        os.remove(destination)
    img.save(destination)

# get dell'immagine
def getSourceImg(target, filename):
    source = "/".join([target, filename])
    return source

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/stringtest")
def test():
    return str("world")

@app.route("/test")
def loadImageFromStatic():
    return send_image('test.jpg')

@app.route("/editandsaveimg")
def editandsaveimg():

    new_filename = "new_img.png"
    target = os.path.join(APP_ROOT, 'static/images')
    source = getSourceImg(target, 'test.jpg')
    img_edited = Image.open(source).convert("L")
    saveImg(img_edited, target, new_filename)

    return send_image(new_filename)

@app.route("/median")
def median():

    new_filename = "median.png"
    target = os.path.join(APP_ROOT, 'static/images')
    source = getSourceImg(target, 'test.jpg')

    img_noisy = Image.open(source).convert("L")

    arr = numpy.array(img_noisy)
    img_median_applied = Image.fromarray(mean_or_median(arr, len(arr), len(arr[0]), "median"))

    saveImg(img_median_applied, target, new_filename)
    
    return send_image(new_filename)


@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory("static/images", filename)

if __name__ == "__main__":
    app.run(debug=True)
