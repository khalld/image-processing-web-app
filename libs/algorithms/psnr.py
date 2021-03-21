import cv2
import numpy
from math import log10, sqrt 

def tmp():
    return "hello world"

def PSNR(path_orig, path_processed):

    original = cv2.imread(path_orig)
    processed = cv2.imread(path_processed)

    mse = numpy.mean((original - processed) ** 2) 
    if(mse == 0):   # MSE is zero means no noise is present in the signal . 
                    # Therefore PSNR have no importance. 
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))


    # print("BEF RETURN....", psnr)

    return psnr

# def main():

#     path = "../../static/images/"

#     print("PSNR VALUE mean 3x3" , PSNR()

# main()