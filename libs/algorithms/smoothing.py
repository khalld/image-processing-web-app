import numpy
from PIL import Image
import cv2
import os

# sostituisce valore di un pixel con il mediano dei livelli di intensità del suo intorno.
# alcuni tipi di rumori casuali hanno capacità di riduzione del rumore, sfocando meno rispetto a quelli di smoothing
# efficaci per rumore a impulsi sia bipolare che unipolare.  Incrementare una finestra si incrementa l'ordine del mediano

# non considero i bordi, li salto completamente

def smoothing_algorithms(input, k, func):
    if (input.mode == "L"):
        return smoothing_op(input,k, func)
    else: # caso RGB
        r, g, b = input.split()

        r = smoothing_op(r, k, func)
        g = smoothing_op(g, k, func)
        b = smoothing_op(b, k, func)

        return Image.merge('RGB', (r, g, b))

def smoothing_op(data, dim_kernel, func):       # require data = PIL.image.image

    data_array = numpy.array(data)

    x_len = numpy.size(data_array,0)

    y_len = numpy.size(data_array,1)

    temp = []

    I = data_array

    for i in range(0, x_len):    # asse x || rows
        for j in range(0, y_len):    # asse y || columns
 
            try:
                # kernel 3x3 fisso!!
                print("PASSO 1 ===> ", I[i-1][j-1] )

                temp.append(I[i-1][j-1])
                temp.append(I[i][j-1])
                temp.append(I[i+1][j-1])

                temp.append(I[i-1][j])
                temp.append(I[i][j])
                temp.append(I[i+1][j])

                temp.append(I[i-1][j+1])
                temp.append(I[i][j+1])
                temp.append(I[i+1][j+1])

                # print("LENNN", temp, len(temp), numpy.median(temp))

                for x in range(i-1, i+1):
                    for y in range(j-1, j+1):
                        print("PASSO 2 *****", I[x][y])

                # print(numpy.median(temp), len(temp), temp)
            except:
                # print("ERRORE GESTITO", temp, len(temp))
                temp = []   # skippiamo!
                continue

            if (func == "mean"):
                I[i][j] = numpy.mean(temp)
            elif (func == "median"):
                I[i][j] = numpy.median(temp)
            temp=[]

    I_ret = Image.fromarray(I)

    return I_ret


def main():

    img_noisy_color = Image.open("../../static/images/test.png")
    img_noisy_color.show(title="original")

    res_mean = smoothing_algorithms(img_noisy_color, 3, "mean")
    res_mean.show()

    res_median = smoothing_algorithms(img_noisy_color, 3, "mean")
    res_median.show()

main()