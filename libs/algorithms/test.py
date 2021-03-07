from remove_noise import remove_noise
from bilateral import bilateral_filter
import numpy as np
from PIL import Image
import imageio


def box(img, r):            # BOX FILTER, img >=2d img, r: radius of box filter

    (rows, cols) = img.shape[:2]
    imDst = np.zeros_like(img)


    tile = [1] * img.ndim
    tile[0] = r
    imCum = np.cumsum(img, 0)
    imDst[0:r+1, :, ...] = imCum[r:2*r+1, :, ...]
    imDst[r+1:rows-r, :, ...] = imCum[2*r+1:rows, :, ...] - imCum[0:rows-2*r-1, :, ...]
    imDst[rows-r:rows, :, ...] = np.tile(imCum[rows-1:rows, :, ...], tile) - imCum[rows-2*r-1:rows-r-1, :, ...]

    tile = [1] * img.ndim
    tile[1] = r
    imCum = np.cumsum(imDst, 1)
    imDst[:, 0:r+1, ...] = imCum[:, r:2*r+1, ...]
    imDst[:, r+1:cols-r, ...] = imCum[:, 2*r+1 : cols, ...] - imCum[:, 0 : cols-2*r-1, ...]
    imDst[:, cols-r: cols, ...] = np.tile(imCum[:, cols-1:cols, ...], tile) - imCum[:, cols-2*r-1 : cols-r-1, ...]

    # print("******\n\n", imDst, "******")

    return imDst


def guided_filter_blackandwhite(I, p, r, eps):  # I = guide image, p: filter input, r: windows radius, eps: regularization

    Isub = I
    Psub = p

    (rows, cols) = Isub.shape # return a tuple with each index having the number of corresponding elements.

    N = box(np.ones([rows, cols]), r)

    meanI = box(Isub, r) / N
    meanP = box(Psub, r) / N
    corrI = box(Isub * Isub, r) / N
    corrIp = box(Isub * Psub, r) / N
    varI = corrI - meanI * meanI
    covIp = corrIp - meanI * meanP

    a = covIp / (varI + eps)
    b = meanP - a * meanI

    meanA = box(a, r) / N
    meanB = box(b, r) / N

    q = meanA * I + meanB
    return q

def main():

    path = "../../static/images/"

    ## *********** INPUT IMG ******* ##
    input_img = Image.open("../../static/images/cat.bmp")
    # input_img.show()

    ## ************ GUIDED ********* ##

    input_guided = np.array(input_img) / 255

    cat_smoothed = guided_filter_blackandwhite(input_guided, input_guided, 8, 0.05)

    imageio.imwrite(path + 'edited/' + 'cat_smoothed.png', cat_smoothed)

    ## *********** BILATERAL ******** ##
    # res_bil = bilateral_filter(input_img, 7, 7, 6.5)
    # res_bil.show()

    ## *********** MEAN / AVERAGE ******* ##
    # res_mean = remove_noise(input_img, 7, "mean")
    # res_mean.show()

    ## *********** MEDIAN ******* ##
    # res_median = remove_noise(input_img, 7, "median")           ## testa noisyimg.png
    # res_median.show()

main()