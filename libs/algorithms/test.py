from remove_noise import remove_noise
from bilateral import bilateral_filter
import numpy
from PIL import Image


def main():

    ## *********** INPUT IMG ******* ##
    input_img = Image.open("../../static/images/noisyimg.png")
    # input_img.show()

    ## *********** BILATERAL ******** ##
    # res_bil = bilateral_filter(input_img, 7, 7, 6.5)
    # res_bil.show()

    ## *********** MEAN / AVERAGE ******* ##
    # res_mean = remove_noise(input_img, 7, "mean")
    # res_mean.show()

    ## *********** MEDIAN ******* ##
    res_median = remove_noise(input_img, 7, "median")           ## testa noisyimg.png
    res_median.show()



main()