import numpy
import cv2

def remove_noise(path, k, func):
    """
    Args:
        path         (str)     path
        dim_kernel   (int)     kernel dimension
        function     (str)     choose mean or median 

    Returns:
        result       (ndarray) output filtered image
        (boolean) if input is wrong for some reason
    """

    if (k % 2) == 0:
        k = k-1

    I = cv2.imread(path).astype(numpy.float32)

    if (I.shape[2] == 3):   ## color
        ## stack: Join a sequence of arrays along a new axis.
        output = numpy.stack([ 
                remove_noise_op( I[:,:,0], k, func ),
                remove_noise_op( I[:,:,1], k, func ),
                remove_noise_op( I[:,:,2], k, func )], axis=2 )     ## axis = The axis in the result array along which the input arrays are stacked.
                                                                    ## note about understand why axis=2 https://www.sharpsightlabs.com/blog/numpy-axes-explained/
                                                                    ## examples making a shape of img 384 × 256 with numpy.stack with: 
                                                                    ## -> axis=1  (256, 3, 384)
                                                                    ## -> axis=2  (256, 384, 3)
        return output

    elif (I.shape[2] == 1): ### bw
        return remove_noise_op( I[:,:], k, func )
    else:
        return False

def remove_noise_op(input_img, dim_kernel, func):       # require data = PIL.image.image
    """
    Args:
        input_img    (ndarray)      input image
        dim_kernel   (int)          kernel dimension
        function     (str)          choose mean or median 

    Returns:
        result       (ndarray)      output filtered image
    """

    # get dimension of image
    x_len = numpy.size(input_img,0)
    y_len = numpy.size(input_img,1)

    temp = []   # array that contains kernel value

    I = input_img
    k = dim_kernel-1    ## needed for make the cicle

    for i in range(0, x_len):    # asse x || rows
        for j in range(0, y_len):    # asse y || columns
            try:                               ## make inside try to catch exception for the borders pixel for example 
                for x in range(i-1, i+k):      ## f.e. 3x3 inspect ... -1, 0, 1 quindi range(i-1,i+2)
                    for y in range(j-1, j+k):
                        temp.append(I[x][y])
            except:
                # print("Error handled", temp, len(temp))
        
                ## consider during the execution only values inside the window, better visivly instead of filling the array with 0 
                ## this implementative choise can cause band
                if (func == "mean"):
                    I[i][j] = numpy.mean(temp)
                elif (func == "median"):
                    I[i][j] = numpy.median(temp)
                
                temp = []
                continue

            if (func == "mean"):
                I[i][j] = numpy.mean(temp)      ## make mean
            elif (func == "median"):
                I[i][j] = numpy.median(temp)    ## make median

            temp=[]         ## make empty the array before move the window

    return I

# def main():
#     ## ******* MEAN AND MEDIAN ******* ##

#     input_img = "../../static/images/noisy/tiger.png"

#     res_mean = remove_noise(input_img, 4, "mean")
#     cv2.imwrite('../../static/images/edited/res.png', res_mean) 

#     res_median = remove_noise(input_img, 4, "median")
#     cv2.imwrite('../../static/images/edited/res.png', res_median) 

# main()