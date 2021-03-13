from remove_noise import remove_noise
from bilateral import bilateral_filter
from guided import guided_filter
from PIL import Image
import imageio
import numpy
import matplotlib.pyplot as plt #importing matplotlib
import cv2
from math import log10, sqrt 

def test_mean_and_median():

    print("trying..")

    ## first example mean
    # input_original = cv2.imread(path + 'test.jpg')

    # fig.canvas.set_window_title('Original image') 
    # plt.hist(input_original.ravel(),256,[0,256]) 
    # plt.show()

    # input_edited = cv2.imread(path + 'edited/mean/mean_3x3.png')

    # fig.canvas.set_window_title('Mean 3x3 histogram') 
    # plt.hist(input_edited.ravel(),256,[0,256]) 
    # plt.show()

    # print("PSNR VALUE", PSNR(input_original, input_edited))

    # print("PSNR VALUE mean 3x3" , PSNR(input_original, cv2.imread(path + 'edited/mean/tiger_3x3.png') ))
    # print("PSNR VALUE mean 5x5" , PSNR(input_original, cv2.imread(path + 'edited/mean/tiger_5x5.png') ))

    ## first example median
    # 
    # 
    # input_original = cv2.imread(path + 'test.jpg')

    # input_edited = cv2.imread(path + 'edited/median/median_3x3.png')

    # fig.canvas.set_window_title('median 3x3 histogram') 
    # plt.hist(input_edited.ravel(),256,[0,256]) 
    # plt.show()

    # print("PSNR VALUE median" , PSNR(input_original, input_edited))
    #   

    ## ****************************+

    ## ******* MEAN AND MEDIAN ******* ##

    # res_median_3 =  remove_noise(input_img, 3, "median")
    # res_median_5 =  remove_noise(input_img, 5, "median")

    # res_mean_3 =  remove_noise(input_img, 3, "mean")
    # res_mean_5 =  remove_noise(input_img, 5, "mean")


    # res_median_3.save(path + 'edited/median/tiger_3x3.png', 'PNG')
    # res_median_5.save(path + 'edited/median/tiger_5x5.png', 'PNG')

    # res_mean_3.save(path + 'edited/mean/tiger_3x3.png', 'PNG')
    # res_mean_5.save(path + 'edited/mean/tiger_5x5.png', 'PNG')

    ## ISTOGRAMMI
    # img_base = cv2.imread(path + '/noisy/tiger.png')

    # fig.canvas.set_window_title('Original image') 
    # plt.hist(img_base.ravel(),256,[0,256]) 
    # plt.show() 

    ## MEAN

    ### 3x3
    # img_mean_3 = cv2.imread(path + '/edited/mean/tiger_3x3.png')
    # plt.hist(img_mean_3.ravel(),256,[0,256]) 
    # fig.canvas.set_window_title('Mean 3x3 applied') 
    # plt.show()

    ### 5x5
    # img_mean_5 = cv2.imread(path + '/edited/mean/tiger_5x5.png')
    # plt.hist(img_mean_5.ravel(),256,[0,256]) 
    # fig.canvas.set_window_title('Mean 5x5 applied') 
    # plt.show()

    ### MEDIAN

    ## 3x3
    # img_median_3 = cv2.imread(path + '/edited/median/tiger_3x3.png')
    # plt.hist(img_median_3.ravel(),256,[0,256]) 
    # fig.canvas.set_window_title('tiger 3x3 histogram') 
    # plt.show()

    ## 5x5
    # img_median_5 = cv2.imread(path + '/edited/median/tiger_5x5.png')
    # plt.hist(img_median_5.ravel(),256,[0,256]) 
    # fig.canvas.set_window_title('tiger 5x5 histogram') 
    # plt.show()


def PSNR(original, compressed): 
    mse = numpy.mean((original - compressed) ** 2) 
    if(mse == 0):   # MSE is zero means no noise is present in the signal . 
                    # Therefore PSNR have no importance. 
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse)) 
    return psnr

def main():

    path = "../../static/images/"
    fig = plt.figure() 



    ## *********** INPUT IMG ******* ##
    # input_img = Image.open(path + "cat.bmp")
    # input_img = Image.open(path + "/noisy/tiger.png")

    ## *********** BILATERAL ******** ##
    # res_bil = bilateral_filter(input_img, 7, 7, 6.5)
    # res_bil.show()

    ## ************ GUIDED ********* ##
    ## bw
    # result_guided = guided_filter(input_img, input_img, 4, 0.05)
    # result_guided.show()

    ## color
    # result_guided_col = guided_filter(input_img_col, input_img_col, 4, 0.05)
    # imageio.imwrite(path + 'edited/guided_color.png', result_guided_col) # NOTA:: altro modo per scrivere sul disco invece di usare open-cv deve ritornare I_Smoothed senza 255, controlla se si può fare pure

    # ======== non funge !!! !!! =========================
    # res_bil_color = Image.fromarray(result_guided_col)
    # res_bil_color.show()

    # print("RESULT COLOR\n\n", result_guided_col, "\n\n" )

    # =============================================

main()