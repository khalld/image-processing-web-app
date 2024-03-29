import cv2
import numpy
# from psnr import PSNR

def filter_bilateral_op( input_img, sigma_d, sigma_r, reg_constant=1e-8 ):
    """
    Args:
        input_img       (ndarray)      monochrome input image or one of channel of image
        sigma_d         (float)        spatial gaussian
        sigma_r         (float)        range of gaussian
        reg_constant    (float)        optional regularization constant for pathalogical cases  

    Returns:
        result          (ndarray)      output bilateral-filtered image
    """

    # simple Gaussian function taking the squared radius (non è l)
    ## https://www.w3schools.com/python/python_lambda.asp
    gaussian = lambda r2, sigma: (numpy.exp( -0.5*r2/sigma**2 )*3).astype(int)*1.0/3.0

    radius = int( 3*sigma_d+1 )                 #window's dimension must be 3 times spatial sigma to be sure most of kernel spatial is considered (cosa sbagliata nella vecchia impl)
    
    # (tips founded) initialize the results and sum of weights to very small values for
    # numerical stability. not strictly necessary but helpful to avoid
    # wild values with pathological choices of parameters 
    wgt_sum = numpy.ones( input_img.shape )*reg_constant       ## denom of function
    result  = input_img*reg_constant

    # scorro secondo le dimensioni della finestra
    for x in range(-radius,radius+1):
        for y in range(-radius,radius+1):                  ## calc weights and compute the result..
            # compute the spatial weight
            w = gaussian( x**2+y**2, sigma_d )             ## ** means exponenzial

            curr_val = numpy.roll(input_img, [y, x], axis=[0,1] )   ## Roll array elements along a given axis. visual example of roll https://www.w3resource.com/numpy/manipulation/roll.php
                                                               ## to have the intensity of pixels of the given img
            
            curr_weight = w*gaussian( (curr_val-input_img)**2, sigma_r )
            result += curr_val*curr_weight
            wgt_sum += curr_weight
    # normalize the result and return
    return result/wgt_sum

def bilateral_filter(path, sigma_d, sigma_r):
    """
    Args:
        path        (str)          path of img
        sigma_d     (float)        spatial gaussian
        sigma_r     (float)        value gaussian
    Returns:
        result      (ndarray)      output bilateral-filtered image
                    (boolean)      if input is wrong for some reason
    """
    ## read image with open-cv and divide by the interval
    I = cv2.imread(path).astype(numpy.float32)/255.0

    if (I.shape[2] == 3):   ## color
        ## stack: Join a sequence of arrays along a new axis.
        output = numpy.stack([ 
                filter_bilateral_op( I[:,:,0], sigma_d, sigma_r ),
                filter_bilateral_op( I[:,:,1], sigma_d, sigma_r ),
                filter_bilateral_op( I[:,:,2], sigma_d, sigma_r )], axis=2 )    ## axis = The axis in the result array along which the input arrays are stacked.

        return output * 255.0

    elif (I.shape[2] == 1): ### bw
        return filter_bilateral_op( I[:,:], sigma_d, sigma_r )
    else:
        return False

# def main():

#     input_img = '../../static/images/test.jpg'

#     #########  sigma_d ==> 2
#     res_bil_1 = bilateral_filter(input_img, 2, 0.1)
#     cv2.imwrite('../../static/images/edited/bilateral/res_bilateral_1.png', res_bil_1) 
#     print("END 1")

#     res_bil_2 = bilateral_filter(input_img, 2, 0.2)
#     cv2.imwrite('../../static/images/edited/bilateral/res_bilateral_2.png', res_bil_2) 
#     print("END 2")

#     res_bil_3 = bilateral_filter(input_img, 2, 0.4)
#     cv2.imwrite('../../static/images/edited/bilateral/res_bilateral_3.png', res_bil_3) 
#     print("END 3")

#     ######### sigma_d ==> 4

#     res_bil_4 = bilateral_filter(input_img, 4, 0.1)
#     cv2.imwrite('../../static/images/edited/bilateral/res_bilateral_4.png', res_bil_4) 
#     print("END 4")

#     res_bil_5 = bilateral_filter(input_img, 4, 0.2)
#     cv2.imwrite('../../static/images/edited/bilateral/res_bilateral_5.png', res_bil_5) 
#     print("END 5")

#     res_bil_6 = bilateral_filter(input_img, 4, 0.4)
#     cv2.imwrite('../../static/images/edited/bilateral/res_bilateral_6.png', res_bil_6) 
#     print("END 6")

#     ######### sigma_d ==> 8

#     res_bil_7 = bilateral_filter(input_img, 4, 0.1)
#     cv2.imwrite('../../static/images/edited/bilateral/res_bilateral_7.png', res_bil_7) 
#     print("END 7")

#     res_bil_8 = bilateral_filter(input_img, 4, 0.2)
#     cv2.imwrite('../../static/images/edited/bilateral/res_bilateral_8.png', res_bil_8) 
#     print("END 8")

#     res_bil_9 = bilateral_filter(input_img, 4, 0.4)
#     cv2.imwrite('../../static/images/edited/bilateral/res_bilateral_9.png', res_bil_9) 
#     print("END 9")

#     ######### PSNR ##########

#     print("RES 1 ===>   ", PSNR(input_img,'../../static/images/edited/bilateral/res_bilateral_1.png')  )
#     print("RES 2 ===>   ", PSNR(input_img,'../../static/images/edited/bilateral/res_bilateral_2.png')  )
#     print("RES 3 ===>   ", PSNR(input_img,'../../static/images/edited/bilateral/res_bilateral_3.png')  )
#     print("RES 4 ===>   ", PSNR(input_img,'../../static/images/edited/bilateral/res_bilateral_4.png')  )
#     print("RES 5 ===>   ", PSNR(input_img,'../../static/images/edited/bilateral/res_bilateral_5.png')  )
#     print("RES 6 ===>   ", PSNR(input_img,'../../static/images/edited/bilateral/res_bilateral_6.png')  )
#     print("RES 7 ===>   ", PSNR(input_img,'../../static/images/edited/bilateral/res_bilateral_7.png')  )
#     print("RES 8 ===>   ", PSNR(input_img,'../../static/images/edited/bilateral/res_bilateral_8.png')  )
#     print("RES 9 ===>   ", PSNR(input_img,'../../static/images/edited/bilateral/res_bilateral_9.png')  )

# main()