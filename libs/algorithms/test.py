from remove_noise import remove_noise
from bilateral import bilateral_filter
from guided import guided_filter
from PIL import Image
import imageio
import numpy
import matplotlib.pyplot as plt #importing matplotlib
import cv2
from math import log10, sqrt 
# from psnr import PSNR

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

def test_bilateral_and_guided():
    path = "../../static/images/"
    fig = plt.figure() 

    ## *********** INPUT IMG ******* ##
    input_img = Image.open(path + "test.jpg")
    # input_img_noisy = Image.open(path + "/noisy/tiger.png")

    ## ***** bilateral *** ##

    #######


    ## **** test guided guided *****

    ### r = 2 
    #               ;;; eps = 0.1 0.2 0.4    
    # res_guid_1 = guided_filter(input_img, 2, 0.01)
    # imageio.imwrite(path + 'edited/guided/res_guid_1.png', res_guid_1) 

    # print("**** END 1")

    # res_guid_2 = guided_filter(input_img, 2, 0.04)
    # imageio.imwrite(path + 'edited/guided/res_guid_2.png', res_guid_2) 

    # print("**** END 2")


    # res_guid_3 = guided_filter(input_img, 2, 0.16)
    # imageio.imwrite(path + 'edited/guided/res_guid_3.png', res_guid_3) 

    # print("**** END 3")

    # ### r = 4;

    # res_guid_4 = guided_filter(input_img, 4, 0.01)
    # imageio.imwrite(path + 'edited/guided/res_guid_4.png', res_guid_4) 

    # print("**** END 4")


    # res_guid_5 = guided_filter(input_img, 4, 0.04)
    # imageio.imwrite(path + 'edited/guided/res_guid_5.png', res_guid_5) 

    # print("**** END 5")


    # res_guid_6 = guided_filter(input_img, 4, 0.16)
    # imageio.imwrite(path + 'edited/guided/res_guid_6.png', res_guid_6) 

    # print("**** END 6")


    # ### r = 8

    # res_guid_7 = guided_filter(input_img, 8, 0.01)
    # imageio.imwrite(path + 'edited/guided/res_guid_7.png', res_guid_7) 

    # print("**** END 7")


    # res_guid_8 = guided_filter(input_img, 8, 0.04)
    # imageio.imwrite(path + 'edited/guided/res_guid_8.png', res_guid_8) 

    # print("**** END 8")


    # res_guid_9 = guided_filter(input_img, 8, 0.16)
    # imageio.imwrite(path + 'edited/guided/res_guid_9.png', res_guid_9) 

    # print("**** END 9")

    ## PSNR test guided .... todo.....
    # input_original = cv2.imread(path + 'test.jpg')

    # print("PSNR VALUE BILATERAL 3, 3, 1.5" , PSNR(input_original, cv2.imread(path + 'edited/bilateral/test_bilateral_1.png') ))


def main():

    path = "../../static/images/"
    fig = plt.figure() 

    test_bilateral_and_guided()

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