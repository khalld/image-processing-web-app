from remove_noise import remove_noise
from bilateral import bilateral_filter
from guided import guided_filter
from PIL import Image
import imageio
import numpy

# def salt_pepper(density):
#     imarray = numpy.random.rand(density,density,3) * 255
#     return Image.fromarray(imarray.astype('uint8')).convert('L')

def main():

    path = "../../static/images/"

    ## *********** INPUT IMG ******* ##
    # input_img = Image.open(path + "cat.bmp")
    input_img = Image.open(path + "test.jpg")

    # res_mean_3 =  remove_noise(input_img, 3, "mean")
    # res_mean_5 =  remove_noise(input_img, 5, "mean")
    # res_mean_7 =  remove_noise(input_img, 7, "mean")
    # res_mean_9 =  remove_noise(input_img, 9, "mean")

    # res_mean_3.save(path + 'edited/mean_3x3.png', 'PNG')
    # res_mean_5.save(path + 'edited/mean_5x5.png', 'PNG')
    # res_mean_7.save(path + 'edited/mean_7x7.png', 'PNG')
    # res_mean_9.save(path + 'edited/mean_9x9.png', 'PNG')

    res_median_3 =  remove_noise(input_img, 3, "median")
    res_median_5 =  remove_noise(input_img, 5, "median")
    res_median_7 =  remove_noise(input_img, 7, "median")
    res_median_9 =  remove_noise(input_img, 9, "median")

    res_median_3.save(path + 'edited/median_3x3.png', 'PNG')
    res_median_5.save(path + 'edited/median_5x5.png', 'PNG')
    res_median_7.save(path + 'edited/median_7x7.png', 'PNG')
    res_median_9.save(path + 'edited/median_9x9.png', 'PNG')

    # input_img.show()



    ## *********** MEAN / AVERAGE ******* ##
    # res_mean = remove_noise(input_img, 7, "mean")
    # res_mean.show()












    ## *********** MEDIAN ******* ##
    # res_median = remove_noise(input_img, 7, "median")           ## testa noisyimg.png
    # res_median.show()

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