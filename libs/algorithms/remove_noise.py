import numpy
from PIL import Image   ## deprecated
import cv2

# sostituisce valore di un pixel con il mediano dei livelli di intensità del suo intorno.
# alcuni tipi di rumori casuali hanno capacità di riduzione del rumore, sfocando meno rispetto a quelli di smoothing
# efficaci per rumore a impulsi sia bipolare che unipolare.  Incrementare una finestra si incrementa l'ordine del mediano

def remove_noise(path, k, func):
    """
    Args:
        path        (str)     path
        dim_kernel   (int)     kernel dimension
        function     (str)     choose mean or median 

    Returns:
        result       (ndarray) output filtered image
    """

    if (k % 2) == 0:
        k = k-1

    I = cv2.imread(path).astype(numpy.float32)

    if (I.shape[2] == 3):   ## color
        ## stack: Join a sequence of arrays along a new axis.
        output = numpy.stack([ 
                remove_noise_op( I[:,:,0], k, func ),
                remove_noise_op( I[:,:,1], k, func ),
                remove_noise_op( I[:,:,2], k, func )], axis=2 )    ## axis = The axis in the result array along which the input arrays are stacked.

        return output

    elif (I.shape[2] == 1): ### bw
        return remove_noise_op( I[:,:], k, func )
    else:
        return False

def remove_noise_op(input_img, dim_kernel, func):       # require data = PIL.image.image

    x_len = numpy.size(input_img,0)
    y_len = numpy.size(input_img,1)

    temp = []

    I = input_img
    k = dim_kernel-1

    for i in range(0, x_len):    # asse x || rows
        for j in range(0, y_len):    # asse y || columns
 
            try:
                # kernel 3x3 ad esempio ispeziona... -1, 0, 1 quindi range(i-1,i+2)
                for x in range(i-1, i+k):
                    for y in range(j-1, j+k):
                        temp.append(I[x][y])
                        # print("ITER: i---->", i, "esaminato", I[i][j], temp, len(temp))                    
            except:
                # print("ERRORE GESTITO", temp, len(temp))
                
                # si inserisce l'except per evitare che l'algoritmo si blocchi ad esempio quando analizza i pixel nei bordi
                # PROVA1: consideriamo solo i pixel all'interno dell'array temp prima di resettarloe  sostitutiamo
                if (func == "mean"):
                    I[i][j] = numpy.mean(temp)
                elif (func == "median"):
                    I[i][j] = numpy.median(temp)

                # PROVA 2: CONSIDERIAMO AGGIUNGIAMO DEGLI 0 DOVE NON VI SONO elementi nell'immagine
                # elem_mancanti = (dim_kernel*dim_kernel) - len(temp)
                # for i in range(0, elem_mancanti):
                #     temp.append(0)


                # da test effettuati il primo caso può causare delle bande uniformi ma è migliore a livello visivo rispetto al secondo 
                
                temp = []
                continue

            if (func == "mean"):
                I[i][j] = numpy.mean(temp)
            elif (func == "median"):
                I[i][j] = numpy.median(temp)

            temp=[]

    I_ret = I

    return I_ret

# def main():
#     ## ******* MEAN AND MEDIAN ******* ##

#     input_img = "../../static/images/cat.bmp"

#     res_mean = remove_noise(input_img, 4, "mean")
#     cv2.imwrite('../../static/images/edited/mean/MEAN_NEW.png', res_mean) 

#     res_median = remove_noise(input_img, 4, "median")
#     cv2.imwrite('../../static/images/edited/mean/MEDIAN_NEW.png', res_median) 

# main()