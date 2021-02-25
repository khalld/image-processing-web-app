import numpy
from PIL import Image
import cv2

# sostituisce valore di un pixel con il mediano dei livelli di intensità del suo intorno.
# alcuni tipi di rumori casuali hanno capacità di riduzione del rumore, sfocando meno rispetto a quelli di smoothing
# efficaci per rumore a impulsi sia bipolare che unipolare.  Incrementare una finestra si incrementa l'ordine del mediano

# non considero i bordi, li salto completamente


def mean_or_median(data, H, W, str):

    I = data

    for i in range(2, W-1):
        for j in range(3, H-1):
            
            temp = []   # array temporaneo che permette di cercare le statistiche d'ordine

            # kernel 3x3 fisso
            temp.append(I[i-1][j-1])
            temp.append(I[i][j-1])
            temp.append(I[i+1][j-1])

            temp.append(I[i-1][j])
            temp.append(I[i][j])
            temp.append(I[i+1][j])

            temp.append(I[i-1][j+1])
            temp.append(I[i][j+1])
            temp.append(I[i+1][j+1])

            if(str == "median"):
                temp.sort()
                I[i][j] = numpy.median(temp)
            else:       # avrei potuto mettere un else if ma al momento non lo reputo necessario in quanto il secondo caso di default è mean
                I[i][j] = numpy.mean(temp)

    return I


# DECOMMENTA SE NECESSARIO TESTARE SINGOLARMENTE
# def main():

#     # Read the image with cv2 || alternativamente a Image
#     # img_noisy1 = cv2.imread('original.jpg', 0) 
    
#     img_noisy = Image.open("../../static/images/test.jpg").convert("L") # Converto l'immagine e la rendo a canale unico    
#     img_noisy.show(title="Original")

#     arr = numpy.array(img_noisy)

#     # applico il filtro
#     removed_noise_median = mean_or_median(arr, len(arr), len(arr[0]), "median")
#     removed_noise_mean = mean_or_median(arr, len(arr), len(arr[0]), "mean")

#     # converto l'array in immagine
#     img_filtered_median = Image.fromarray(removed_noise_median)
#     img_filtered_mean = Image.fromarray(removed_noise_mean)


#     img_filtered_median.show(title="Median")        # NB: non funziona il title! Fixa!
#     img_filtered_mean.show(title="Mean")

#     #save image elaborated with cv2
#     cv2.imwrite('../../static/images/edited/median.png', removed_noise_median)
#     cv2.imwrite('../../static/images/edited/mean.png', removed_noise_mean)       ## per salvarlo



# main()