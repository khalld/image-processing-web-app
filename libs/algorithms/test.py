from remove_noise import remove_noise
from bilateral import bilateral_filter
from guided import guided_filter
from PIL import Image
import imageio

def main():

    path = "../../static/images/"

    ## *********** INPUT IMG ******* ##
    input_img = Image.open(path + "cat.bmp")
    input_img_col = Image.open(path + "test.png")

    # input_img.show()

    ## ************ GUIDED ********* ##
    ## bw
    # result_guided = guided_filter(input_img, input_img, 4, 0.05)
    # result_guided.show()

    ## color
    result_guided_col = guided_filter(input_img_col, input_img_col, 4, 0.05)
    imageio.imwrite(path + 'edited/guided_color.png', result_guided_col) # NOTA:: altro modo per scrivere sul disco invece di usare open-cv deve ritornare I_Smoothed senza 255, controlla se si può fare pure

    # non funge !!! !!!
    # res_bil_color = Image.fromarray(result_guided_col)
    # res_bil_color.show()

    # print("RESULT COLOR\n\n", result_guided_col, "\n\n" )


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