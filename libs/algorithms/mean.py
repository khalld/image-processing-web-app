import numpy
from PIL import Image

# sostituisce valore di un pixel con il mediano dei livelli di intensità del suo intorno.
# alcuni tipi di rumori casuali hanno capacità di riduzione del rumore, sfocando meno rispetto a quelli di smoothing
# efficaci per rumore a impulsi sia bipolare che unipolare.  Incrementare una finestra si incrementa l'ordine del mediano

# non considero i bordi, li salto completamente

def mean_old(data, dim_kernel):       # require data = PIL.image.image

    data_array = numpy.array(data)

    H = len(data_array)
    W = len(data_array[0])

    I = data_array

    kernel_dim_x = 0
    kernel_dim_y = 0

    if(H == W):
        print("uguale")
        kernel_dim_x = kernel_dim_y = W % dim_kernel

    else:
        # come devo gestirmi questo caso?? nel caso in cui le img sono diverse da
        return False

    for i in range(kernel_dim_x, W-1):    # asse x || rows

        for j in range(kernel_dim_y, H-1):    # asse y || columns

            temp = []   # array temporaneo che permette di cercare le statistiche d'ordine

            # # # kernel 3x3 fisso
            temp.append(I[i][j-1])
            temp.append(I[i][j])
            temp.append(I[i][j+1])

            temp.append(I[i+1][j-1])
            temp.append(I[i+1][j])
            temp.append(I[i+1][j+1])
            
            temp.append(I[i-1][j-1])
            temp.append(I[i-1][j])
            temp.append(I[i-1][j+1])


            I[i][j] = numpy.mean(temp)

    I_ret = Image.fromarray(I)

    return I_ret


def main():
    # IMMAGINI A UN SOLO CANALE (CONVERTITE) CON PILLOW
    
    # img_noisy = Image.open("../../static/images/test_rumore.png").convert("L") # Converto l'immagine e la rendo a canale unico    
    # img_noisy = Image.open("../../static/images/test.jpg").convert("L") # Converto l'immagine e la rendo a canale unico    
    # img_noisy.show(title="Original")

    # removed_noise_mean= mean_old(img_noisy, 3)

    # removed_noise_mean.show(title="Mean3")

    # ******* IMMAGINI A COLORI **************

    img_noisy_color = Image.open("../../static/images/test.png")
    img_noisy_color.show(title="original")

    r, g, b = img_noisy_color.split()

    # r.show()
    # b.show()
    # g.show()
    
    r = mean_old(r, 3)
    g = mean_old(g, 3)
    b = mean_old(b, 3)

    result = Image.merge('RGB', (r, g, b))
    result.show()

main()