from remove_noise import remove_noise_algorithms
from bilateral import bilateral_filter
import numpy
from PIL import Image


def main():

    input_img = Image.open("../../static/images/test.png").convert("L")
    # input_img.show()

    res_bil = bilateral_filter(input_img, 7, 7, 6.5)
    res_bil.show()

    # res_3_mean = remove_noise_algorithms(input_img, 3, "mean")
    # res_3_mean.show()

    # res_3_median = remove_noise_algorithms(input_img, 3, "median")
    # res_3_median.show()
    
    # res_5 = remove_noise_algorithms(Image.open("../../static/images/noisyimg.png"), 5, "median")
    # res_5.show()

    # res_8 = remove_noise_algorithms(Image.open("../../static/images/noisyimg.png"), 8, "median")
    # res_8.show()



main()