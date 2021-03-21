import cv2
import numpy
import random
import imageio
import visvis as vv
# from psnr import PSNR

# i = 0             ## test

# def incr():       ### test
#     global i
#     i = i+1

## size of kernel dictates how many pixels in some NxN neighborhood to be calculated together.
## this function returns all the values inside a window of dimension r
def box(img, r):            # BOX FILTER, img >=2d img, r: radius of box filter

    # print("ENTER HERE", i)        ## test
    # incr()                        ## test

    (rows, cols) = img.shape[:2]
    imDst = numpy.zeros_like(img)

    # Note: The [:, :] stands for everything from the beginning to the end just like for lists. first for first and second dimensions

    ## rows
    tile = [1] * img.ndim
    tile[0] = r
    imCum = numpy.cumsum(img, 0)        ### cumsum Return the cumulative sum of the elements along a given axis.
    imDst[0:r+1, :, ...] = imCum[r:2*r+1, :, ...]
    imDst[r+1:rows-r, :, ...] = imCum[2*r+1:rows, :, ...] - imCum[0:rows-2*r-1, :, ...]
    imDst[rows-r:rows, :, ...] = numpy.tile(imCum[rows-1:rows, :, ...], tile) - imCum[rows-2*r-1:rows-r-1, :, ...]     ## numpy.tile(A, reps)[source] Construct an array by repeating A the number of times given by reps.

    ## columns
    tile = [1] * img.ndim
    tile[1] = r
    imCum = numpy.cumsum(imDst, 1)
    imDst[:, 0:r+1, ...] = imCum[:, r:2*r+1, ...]
    imDst[:, r+1:cols-r, ...] = imCum[:, 2*r+1 : cols, ...] - imCum[:, 0 : cols-2*r-1, ...]
    imDst[:, cols-r: cols, ...] = numpy.tile(imCum[:, cols-1:cols, ...], tile) - imCum[:, cols-2*r-1 : cols-r-1, ...]

    # print("******\n\n", imDst, "******")

    # imageio.imwrite('../../static/images/edited/guided/testbox/box_' + str(i) + '.png', imDst)

    return imDst

# implemented algorithm for bw image from the paper in the source
def guided_filter_blackandwhite(I, p, r, eps):  # I = guide image, p: filter input, r: windows radius, eps: regularization
    """
    Args:
        I       (array)         input img
        p       (array)         guidance image
        r       (int)           radius of window
        eps     (float)         regularization
    Returns:
        q       (array)         result of equation
    """

    Isub = I
    Psub = p

    rows = Isub.shape[0]
    cols = Isub.shape[1]

    N = box(numpy.ones([rows, cols]), r)        ## number of elements  and .ones Return a new array of given shape and type, filled with ones

    ## part 1
    meanI = box(Isub, r) / N                    ## fmean(I)
    meanP = box(Psub, r) / N                    ## fmean(p)

    corrI = box(Isub * Isub, r) / N             ## fmean(I.*I)
    corrIp = box(Isub * Psub, r) / N            ## fmean(I.*p)

    ## part2
    varI = corrI - meanI * meanI
    covIp = corrIp - meanI * meanP

    ## part3
    a = covIp / (varI + eps)
    b = meanP - a * meanI

    ## part4
    meanA = box(a, r) / N                       ## fmean(a)
    meanB = box(b, r) / N                       ## fmean(b)

    q = meanA * I + meanB

    return q

## implemented algorithm for color image from the paper in the source
def guided_filter_color(I, p, r, eps):      # I guide image, p filtering input, r windows radius, eps regularization
    """
    Args:
        I       (array)         input img
        p       (array)         guidance image
        r       (int)           radius of window
        eps     (float)         regularization
    Returns:
        q       (array) result of equation
    """

    fullI = I
    fullP = p

    rows = fullI.shape[0]
    cols = fullI.shape[1]

    N = box(numpy.ones((cols, rows)), r)
    meanPatch = box(p, r) / N                      ## patch

    ## part 1 
    meanI_r = box(I[:,:,0], r) / N
    meanI_g = box(I[:,:,1], r) / N
    meanI_b = box(I[:,:,2], r) / N

    # compute mean of I * p
    meanIp_r = box(I[:,:,0]*p, r) / N
    meanIp_g = box(I[:,:,1]*p, r) / N
    meanIp_b = box(I[:,:,2]*p, r) / N

    # per-patch covarianza di (I, p)
    covIp_r = meanIp_r - meanI_r * meanPatch
    covIp_g = meanIp_g - meanI_g * meanPatch
    covIp_b = meanIp_b - meanI_b * meanPatch

    # compute symmetric covariance of I matrix for every pixels of every patch:
    var_I_rr = box(I[:,:,0] * I[:,:,0], r) / N - meanI_r * meanI_r
    var_I_rg = box(I[:,:,0] * I[:,:,1], r) / N - meanI_r * meanI_g
    var_I_rb = box(I[:,:,0] * I[:,:,2], r) / N - meanI_r * meanI_b

    var_I_gg = box(I[:,:,1] * I[:,:,1], r) / N - meanI_g * meanI_g
    var_I_gb = box(I[:,:,1] * I[:,:,2], r) / N - meanI_g * meanI_b

    var_I_bb = box(I[:,:,2] * I[:,:,2], r) / N - meanI_b * meanI_b

    a = numpy.zeros((cols, rows, 3))
    for i in range(cols):
        for j in range(rows):
            sig = numpy.array([
                [var_I_rr[i,j], var_I_rg[i,j], var_I_rb[i,j]],
                [var_I_rg[i,j], var_I_gg[i,j], var_I_gb[i,j]],
                [var_I_rb[i,j], var_I_gb[i,j], var_I_bb[i,j]]
            ])
            covIp = numpy.array([covIp_r[i,j], covIp_g[i,j], covIp_b[i,j]])
            a[i,j,:] = numpy.linalg.solve(sig + eps * numpy.eye(3), covIp)      ## .eye Return a 2-D array with ones on the diagonal and zeros elsewhere.

    b = meanPatch - a[:,:,0] * meanI_r - a[:,:,1] * meanI_g - a[:,:,2] * meanI_b

    meanA = box(a, r) / N[...,numpy.newaxis]        ##  increase the dimension of the existing array by one more dimension
    meanB = box(b, r) / N

    q = numpy.sum(meanA * fullI, axis=2) + meanB

    return q

# def guided_filter(I, p, r, eps):    ### I input image , guidance image g, radius r, regularization eps
## by default the guidance image is the same of input
def guided_filter(path, r, eps):
    """
        Args:
            path    (str)    path of input image
            r       (int)    radius
            eps     (str)    regularization 
        Returns:
            result       (ndarray) output filtered image
    """

    ## read image with imageio and divide by the interval   (if use opencv2 the result would be of different colors)
    I = imageio.imread(path).astype(numpy.float32)/255.0

    try:
        ## best founded way to handle b/w images
        I_smoothed = numpy.zeros_like(I)  # smoothed array
        for i in range(3):
            I_smoothed[:,:,i] = guided_filter_color(I, I[:,:,i], r, eps)
    
        return I_smoothed
    except:
        # print("exception occurred, is a bw file")
        return guided_filter_blackandwhite( I[:,:], I[:,:], r, eps )

# def main():
#     input_img = "../../static/images/test.jpg"

#     print("RES 1 ===>   ", PSNR(input_img,'../../static/images/edited/guided/res_guid_1.png')  )
#     print("RES 2 ===>   ", PSNR(input_img,'../../static/images/edited/guided/res_guid_2.png')  )
#     print("RES 3 ===>   ", PSNR(input_img,'../../static/images/edited/guided/res_guid_3.png')  )
#     print("RES 4 ===>   ", PSNR(input_img,'../../static/images/edited/guided/res_guid_4.png')  )
#     print("RES 5 ===>   ", PSNR(input_img,'../../static/images/edited/guided/res_guid_5.png')  )
#     print("RES 6 ===>   ", PSNR(input_img,'../../static/images/edited/guided/res_guid_6.png')  )
#     print("RES 7 ===>   ", PSNR(input_img,'../../static/images/edited/guided/res_guid_7.png')  )
#     print("RES 8 ===>   ", PSNR(input_img,'../../static/images/edited/guided/res_guid_8.png')  )
#     print("RES 9 ===>   ", PSNR(input_img,'../../static/images/edited/guided/res_guid_9.png')  )

# main()