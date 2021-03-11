import numpy
from PIL import Image

# sostituisce valore di un pixel con il mediano dei livelli di intensità del suo intorno.
# alcuni tipi di rumori casuali hanno capacità di riduzione del rumore, sfocando meno rispetto a quelli di smoothing
# efficaci per rumore a impulsi sia bipolare che unipolare.  Incrementare una finestra si incrementa l'ordine del mediano

def remove_noise(input, k, func):

    if (k % 2) == 0:
        k = k-1

    if (input.mode == "L"):
        return remove_noise_op(input,k, func)
    else: # caso RGB
        r, g, b = input.split()

        r = remove_noise_op(r, k, func)
        g = remove_noise_op(g, k, func)
        b = remove_noise_op(b, k, func)

        return Image.merge('RGB', (r, g, b))

def remove_noise_op(data, dim_kernel, func):       # require data = PIL.image.image

    data_array = numpy.array(data)
    x_len = numpy.size(data_array,0)
    y_len = numpy.size(data_array,1)

    temp = []

    I = data_array
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

    I_ret = Image.fromarray(I)

    return I_ret