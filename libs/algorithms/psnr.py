import cv2
import numpy
from math import log10, sqrt 

def PSNR(path_orig, path_processed):

    original = cv2.imread(path_orig)
    processed = cv2.imread(path_processed)

    mse = numpy.mean((original - processed) ** 2) 
    if(mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))

    return psnr

# def main():
#     path = "../../static/images/"
#     print("PSNR VALUE mean 3x3" , PSNR()
# main()