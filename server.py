from flask import Flask, send_from_directory, send_file
import random
import numpy
from PIL import Image
import cv2
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

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
    # stringa = "world"
    # return str(stringa)
    return str("world")


@app.route("/test")
def median():

    # open images
    target = os.path.join(APP_ROOT, 'static/images')
    filename = 'test.jpg'
    source = "/".join([target, filename])


    # return send_file(destination, mimetype='image/gif')
    return send_file(source, mimetype='image/gif')





if __name__ == "__main__":
    app.run(debug=True)
