import numpy
from PIL import Image

# sostituisce valore di un pixel con il mediano dei livelli di intensità del suo intorno.
# alcuni tipi di rumori casuali hanno capacità di riduzione del rumore, sfocando meno rispetto a quelli di smoothing
# efficaci per rumore a impulsi sia bipolare che unipolare.  Incrementare una finestra si incrementa l'ordine del mediano

# non considero i bordi, li salto completamente

# def median(data, H, W, str):
def median(input_img, str):   ## credo che puoi togliere H e W che li prende in auto!

    if(str == "L"):
        print("converti ad un canale...")
        
        input_img.convert("L")
        data = numpy.array(input_img)

        w = len(data)
        h = len(data[0])
    else:
        print("converto analizzando i 3 canali")
        r, g, b = input_img.split()

    I = data

    for i in range(2, w-1):
        for j in range(3, h-1):
            
            temp = []   # array temporaneo che permette di cercare le statistiche d'ordine

            temp.append(I[i-1][j-1])
            temp.append(I[i][j-1])
            temp.append(I[i+1][j-1])

            temp.append(I[i-1][j])
            temp.append(I[i][j])
            temp.append(I[i+1][j])

            temp.append(I[i-1][j+1])
            temp.append(I[i][j+1])
            temp.append(I[i+1][j+1])

            # kernel 3x3 fisso
            # for x in range(i-1, i+1):
            #     for y in range(j-1,j+1):
            #         temp.append(I[x][y])
            temp.sort()
            I[i][j] = numpy.median(temp)

    return I


def main():

    ## IMMAGINI A UN SOLO CANALE (CONVERTITE) CON PILLOW
    
    # img_noisy = Image.open("../../static/images/test.jpg").convert("L") # Converto l'immagine e la rendo a canale unico    
    img_noisy = Image.open("../../static/images/test.jpg")
    img_noisy.show(title="Original")

    removed_noise = median(img_noisy, "L")
    
    result1 = Image.fromarray(removed_noise)

    result1.show()

    # arr = numpy.array(img_noisy)
    
    ## applico il filtro
    # removed_noise_median = median( arr, len(arr), len(arr[0]) )
    
    ## converto l'array in immagine
    # img_filtered_median = Image.fromarray(removed_noise_median)
    
    # img_filtered_median.show(title="Median")

    # ******* IMMAGINI A COLORI **************

    img_noisy_color = Image.open("../../static/images/test.png")
    # img_noisy_color.show(title="original")

    r, g, b = img_noisy_color.split()

    # r.show()
    # b.show()
    # g.show()

    r = numpy.array(r)
    g = numpy.array(g)
    b = numpy.array(b)
    
    r = Image.fromarray(median(r, len(r), len(r[0])))
    g = Image.fromarray(median(g, len(g), len(g[0])))
    b = Image.fromarray(median(b, len(b), len(b[0])))

    result = Image.merge('RGB', (r, g, b))

    result.show()

main()