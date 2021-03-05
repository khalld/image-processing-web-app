import numpy
from PIL import Image
import cv2

# sostituisce valore di un pixel con il mediano dei livelli di intensità del suo intorno.
# alcuni tipi di rumori casuali hanno capacità di riduzione del rumore, sfocando meno rispetto a quelli di smoothing
# efficaci per rumore a impulsi sia bipolare che unipolare.  Incrementare una finestra si incrementa l'ordine del mediano

# non considero i bordi, li salto completamente

def mean(input, k):
    if (input.mode == "L"):
        return mean_old(input,k)
    else: # caso RGB
        r, g, b = input.split()

        r = mean_old(r, k)
        g = mean_old(g, k)
        b = mean_old(b, k)

        return Image.merge('RGB', (r, g, b))
    

def mean_old(data, dim_kernel):       # require data = PIL.image.image

    data_array = numpy.array(data)

    x_len = numpy.size(data_array,0)

    y_len = numpy.size(data_array,1)

    temp = []

    I = data_array

    for i in range(0, x_len):    # asse x || rows
        for j in range(0, y_len):    # asse y || columns
 
            try:
                # kernel 3x3 fisso!!
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

                # print(numpy.median(temp), len(temp), temp)
            except:
                # print("ERRORE GESTITO", temp, len(temp))
                temp = []   # skippiamo!
                continue

            I[i][j] = numpy.mean(temp)
            temp=[]

    I_ret = Image.fromarray(I)

    return I_ret


def main():
    # IMMAGINI A UN SOLO CANALE (CONVERTITE) CON PILLOW
    
    # img_noisy = Image.open("../../static/images/test_rumore.png")# Converto l'immagine e la rendo a canale unico    
    img_noisy = Image.open("../../static/images/noisyimg.png").convert("L") # Converto l'immagine e la rendo a canale unico    
    # img_noisy.show(title="Original")

    removed_noise_mean = mean(img_noisy, 3)
    removed_noise_mean.show(title="Mean3")

    # ******* IMMAGINI A COLORI **************

    img_noisy_color = Image.open("../../static/images/test.png")
    img_noisy_color.show(title="original")

    res_color = mean(img_noisy_color, 3)
    res_color.show()

main()