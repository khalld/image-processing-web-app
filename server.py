from flask import Flask, send_from_directory, send_file, request
import random
import numpy
from PIL import Image
import cv2
import os
from libs.algorithm.mean_or_median import mean_or_median
from libs.utils import saveImg, getSourceImg, cleanbase64

import base64
from io import BytesIO

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
    return str("world")

@app.route("/test")
def loadImageFromStatic():
    return send_image('test.jpg')

@app.route("/editandsaveimg")
def editandsaveimg():

    new_filename = "edited/new_img.png"
    target = os.path.join(APP_ROOT, 'static/images')
    source = getSourceImg(target, 'test.jpg')
    img_edited = Image.open(source).convert("L")
    saveImg(img_edited, target, new_filename)

    return send_image(new_filename)

@app.route("/median")
def median():

    new_filename = "edited/median.png"
    target = os.path.join(APP_ROOT, 'static/images')
    source = getSourceImg(target, 'test.jpg')

    img_noisy = Image.open(source).convert("L")

    arr = numpy.array(img_noisy)
    img_median_applied = Image.fromarray(mean_or_median(arr, len(arr), len(arr[0]), "median"))

    saveImg(img_median_applied, target, new_filename)

    return send_image(new_filename)

@app.route("/mean")
def mean():

    new_filename = "edited/mean.png"
    target = os.path.join(APP_ROOT, 'static/images')
    source = getSourceImg(target, 'test.jpg')

    img_noisy = Image.open(source).convert("L")

    arr = numpy.array(img_noisy)
    img_median_applied = Image.fromarray(mean_or_median(arr, len(arr), len(arr[0]), "mean"))

    saveImg(img_median_applied, target, new_filename)

    return send_image(new_filename)


# TO DO *+++++++++++++#
@app.route("/uploadtest", methods=["POST"])
def uploadtest():

    # il tipo è byte quindi devo fare il cast
    # print(type(request.get_data()))
    # print(request.get_data().decode())

    # base64 = cleanbase64(str(request.get_data()))

    # image_data = request.get_data()

    image_data = BytesIO(request.get_data())
    # image.save(image_data, 'res.png')

    img = Image.frombytes("L", (3, 2), image_data)
    print(img)

    # print(image_data)
    # print(type(imageData.decode()))

    # img = Image.open(imageData.encode())

    # img.save('image.jpg')

    # print(img)


    return str("aaaaaa")

# upload selected image and forward to processing page
@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'static/images/')

    # create image directory if not found
    if not os.path.isdir(target):
        os.mkdir(target)

    # retrieve file from html file-picker
    upload = request.files.getlist("file")[0]
    print("File name: {}".format(upload.filename))
    filename = upload.filename

    # file support verification
    ext = os.path.splitext(filename)[1]
    if (ext == ".jpg") or (ext == ".png") or (ext == ".bmp"):
        print("File accepted")
    else:
        return render_template("error.html", message="The selected file is not supported"), 400

    # save file
    destination = "/".join([target, filename])
    print("File saved to to:", destination)
    upload.save(destination)

    # forward to processing page
    return render_template("processing.html", image_name=filename)

@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory("static/images", filename)

if __name__ == "__main__":
    app.run(debug=True)
