import numpy
from PIL import Image
import cv2


def bilateral(data, H, W, str):

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
def main():

    img = cv2.imread('../../static/images/test.jpg') 
    
    # Apply bilateral filter with d = 15,
    # sigmaColor = sigmaSpace = 75.
    bilateral = cv2.bilateralFilter(img, 15, 75, 75)
    
    # Save the output.
    cv2.imwrite('../../static/images/edited/bilateral.jpg', bilateral)

main()