import numpy as np
from PIL import Image
import math

def bilateral_filter(input, radius, sigma_d, sigma_r):
    if (input.mode == "L"):
        print("L")
        return bilateral_filter_op(input, radius, sigma_d, sigma_r)
    else:
        print("RGB")

# Pseudocodice spiegato nel .md file
def find_weight(i,j,d,I,sigma_d,sigma_r):
    arr=[]
    sum_num=0
    sum_den=0
    for k in range(i-math.floor(d/2),i+math.ceil(d/2)):
        for l in range(j-math.floor(d/2),j+math.ceil(d/2)):

            term1 = ( ((i-k)**2)+(j-l)**2)/(sigma_d**2*2 )
            term2 = ( np.absolute(I[i,j]-I[k,l]) ) / sigma_r**2*2

            term=term1+term2
            w = math.exp(-term)
            arr.append(w)
            sum_num = sum_num+(I[k,l]*w)
            sum_den = sum_den+w

    return sum_num/sum_den

def bilateral_filter_op(input_img, radius, sigma_d, sigma_r):

    I = np.asarray(input_img, dtype="uint8")
    data = I
    I = np.lib.pad(I, 1, 'mean')
    I_new = np.copy(data)

    for i in range(1,data.shape[0]):        # asse x
        for j in range(1,data.shape[1]):    # asse y 
            I_new[i-1,j-1]=find_weight(i-1,j-1,radius,I,sigma_d,sigma_r)
        
    image_new = Image.fromarray(I_new)

    return image_new


def main():

    path = '../../static/images/'

    img = Image.open(path + 'test.png').convert('L')        # linux da il warning perché la apre stranamente con il programma di default, l'originale è in jpg! 



    # img.show()

    # image_new = bilateral_filter(img, 7,7,6.5)

    # image_new.show()

main()