import numpy as np
from PIL import Image
import cv2
import math


# Bilateral filter

# https://teamwisp.github.io/research/bilateral_filter.html
# https://en.wikipedia.org/wiki/Bilateral_filter

# Da scrivere la descrizione ......

#The Bilateral Filter Function. The pseudocode was taken from Wikipedia and written in python
def bilateral_filter(i,j,d,I,sigma_d,sigma_r):
    arr=[]
    sum_num=0
    sum_den=0
    for k in range(i-math.floor(d/2),i+math.ceil(d/2)):
        for l in range(j-math.floor(d/2),j+math.ceil(d/2)):
            term1=(((i-k)**2)+(j-l)**2)/(sigma_d**2*2)

            term2a = np.absolute(I[i,j]-I[k,l])       ## Runtime warning
            term2b = sigma_r**2*2
            term2 = term2a/term2b

            term=term1+term2
            w=math.exp(-term)
            arr.append(w)
            sum_num=sum_num+(I[k,l]*w)
            sum_den=sum_den+w      
    return sum_num/sum_den


def main():

    path = '../../static/images/'

    img = Image.open(path + 'test.png').convert('L')        # linux da il warning perché la apre stranamente con il programma di default, l'originale è in jpg! 

    # img.load()
    # img.show()

    radius = 7

    # I = np.array(img)
    I = np.asarray( img, dtype="uint8" )

    data = I

    I=np.lib.pad(I, 1, 'mean')

    I_new=np.copy(data)

    for i in range(1,data.shape[0]):
        for j in range(1,data.shape[1]):
            I_new[i-1,j-1]=bilateral_filter(i-1,j-1,radius,I,7,6.5)

    image_new = Image.fromarray(I_new)

    # cv2.imwrite(path + '/edited/bilateral_mine.png', image_new)       # Perchè non funge?
    image_new.show()

    #WITH OPENCV lib

    img_cv2 = cv2.imread(path + 'test.png')

    # Apply bilateral filter with d = 15,
    # sigmaColor = sigmaSpace = 75.
    bilateral = cv2.bilateralFilter(img_cv2, 15, 75, 75)
    
    img_bilateral = Image.fromarray(bilateral)

    image_new.show()
    
    # Save the output.
    # cv2.imwrite(path + '/edited/bilateral_cv2.png', bilateral)

main()