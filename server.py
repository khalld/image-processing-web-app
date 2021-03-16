from flask import Flask, send_from_directory, send_file, request
import random
import numpy
from PIL import Image
import imageio
import os
import cv2
from libs.algorithms.remove_noise import remove_noise
from libs.algorithms.bilateral import bilateral_filter
from libs.algorithms.guided import guided_filter

from libs.utils import getSourceImg, getI420FromBase64

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

target = os.path.join(APP_ROOT, 'static/images')

targetUpload = os.path.join(APP_ROOT, 'static/images/app/')

new_filename = "app/processed.png"

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/upload", methods=["POST"])
def upload():
    data_req = request.get_json()
    imgdata = getI420FromBase64(data_req['image'])

    filename = 'static/images/app/uploaded.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)

    return send_from_directory("static/images/app/", "uploaded.png")

@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory("static/images", filename)


@app.route("/mean", methods=["POST"])
def mean():

    req = request.get_json()

    result = remove_noise(targetUpload + 'uploaded.png', req['kernel_dim'], "mean")
    cv2.imwrite(target + '/' + new_filename, result)
    return send_image(new_filename)

@app.route("/median", methods=["POST"])
def median():

    req = request.get_json() # dict type

    result = remove_noise(targetUpload + 'uploaded.png', req['kernel_dim'], "median")
    cv2.imwrite(target + '/' + new_filename, result)

    return send_image(new_filename)

@app.route("/bilateral", methods=["POST"])
def bilateral():

    req = request.get_json()

    sigma_d = req['sigma_d']
    sigma_r = req['sigma_r']

    # input_img = Image.open(getSourceImg(targetUpload, 'uploaded.png'))
    result = bilateral_filter(targetUpload + 'uploaded.png', sigma_d, sigma_r)
    cv2.imwrite(target + '/' + new_filename, result)

    return send_image(new_filename)

@app.route("/guided", methods=["POST"])
def guided():
    req = request.get_json()

    radius = req['radius']
    eps = req['eps']

    input_img = Image.open(getSourceImg(targetUpload, 'uploaded.png'))
    result = guided_filter(input_img, radius, eps)
    imageio.imwrite(target + '/' + new_filename, result) 

    return send_image(new_filename)

@app.route("/psnr", methods=["get"])
def psnr():
    # uploaded = cv2.imread(targetUpload + 'upload.png')
    # processed = cv2.imread(targetUpload + 'processed.png')

    # mse = numpy.mean(( uploaded - processed ) ** 2) 
    # if(mse == 0):   # MSE is zero means no noise is present in the signal . 
    #                 # Therefore PSNR have no importance. 
    #     return str(100)
    
    # max_pixel = 255.0
    # psnr = 20 * log10(max_pixel / sqrt(mse)) 
    # return str(psnr)

    # print("PSNR", psnr)
    return str("this is a strrr")


if __name__ == "__main__":
    app.run(debug=True)
