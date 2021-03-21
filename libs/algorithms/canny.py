import numpy
import os 
import cv2

def convert_bw(img):
    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def noise_red(img, kernel_dim):
    return cv2.GaussianBlur(img, (kernel_dim,kernel_dim), cv2.BORDER_DEFAULT)                 ## setted by default sigmaX=simgaY

def prepare_img(img, kernel_dim):           ## phase 1: noise red
    img = convert_bw(img)
    img = noise_red(img, kernel_dim)
    return img

def double_thresholding(w, h, mag, l_th, h_th):
    for i_x in range(w): 
        for i_y in range(h):
              
            grad_mag = mag[i_y, i_x] 
              
            if grad_mag<l_th: 
                mag[i_y, i_x]= 0

def canny(path, kernel_dim, lower_threshold, higher_threshold): 
    img = cv2.imread(path)                                          ## read image from path
    img = prepare_img(img, kernel_dim)

    # calc gradient apply sobel
    gx = cv2.Sobel(numpy.float32(img), cv2.CV_64F, 1, 0, 3)         ## CV_64F is a grayscale image
    gy = cv2.Sobel(numpy.float32(img), cv2.CV_64F, 0, 1, 3) 
    
    # from cartesian coord to polar
    magnitude, angulation = cv2.cartToPolar(gx, gy, angleInDegrees = True)

    height = img.shape[0]
    width = img.shape[1]

    for i_x in range(width): 
        for i_y in range(height): 
               
            grad_ang = angulation[i_y, i_x] 
            grad_ang = abs(grad_ang-180) if abs(grad_ang)>180 else abs(grad_ang) 
               
            # selecting the neighbours of the target pixel:

            if grad_ang<= 22.5:                                     ## x axis
                neighb_1_x, neighb_1_y = i_x-1, i_y 
                neighb_2_x, neighb_2_y = i_x + 1, i_y 
              
            elif grad_ang>22.5 and grad_ang<=(22.5 + 45):           ## diag-1 (top-right)
                neighb_1_x, neighb_1_y = i_x-1, i_y-1
                neighb_2_x, neighb_2_y = i_x + 1, i_y + 1
              
            elif grad_ang>(22.5 + 45) and grad_ang<=(22.5 + 90):    ## y axis
                neighb_1_x, neighb_1_y = i_x, i_y-1
                neighb_2_x, neighb_2_y = i_x, i_y + 1
              
            elif grad_ang>(22.5 + 90) and grad_ang<=(22.5 + 135):   ## diag-2 (top-left)
                neighb_1_x, neighb_1_y = i_x-1, i_y + 1
                neighb_2_x, neighb_2_y = i_x + 1, i_y-1
              
            elif grad_ang>(22.5 + 135) and grad_ang<=(22.5 + 180): 
                neighb_1_x, neighb_1_y = i_x-1, i_y 
                neighb_2_x, neighb_2_y = i_x + 1, i_y
            
            if width>neighb_1_x>= 0 and height>neighb_1_y>= 0:       # non-maximum supprr
                if magnitude[i_y, i_x]<magnitude[neighb_1_y, neighb_1_x]: 
                    magnitude[i_y, i_x]= 0
   
            if width>neighb_2_x>= 0 and height>neighb_2_y>= 0: 
                if magnitude[i_y, i_x]<magnitude[neighb_2_y, neighb_2_x]: 
                    magnitude[i_y, i_x]= 0
    
    double_thresholding(width, height, magnitude, lower_threshold, higher_threshold)

    return magnitude    ## magnitude of gradients of edges
   

def main():
    canny_1 = canny('../../static/images/test.jpg', 3, 0.1, 0.8)
    canny_2 = canny('../../static/images/test.jpg', 5, 0.1, 0.8)
    canny_3 = canny('../../static/images/test.jpg', 7, 0.1, 0.8)
    canny_4 = canny('../../static/images/test.jpg', 9, 0.1, 0.8)

    cv2.imwrite('../../static/images/edited/canny/canny_1.png', canny_1)
    cv2.imwrite('../../static/images/edited/canny/canny_2.png', canny_2)
    cv2.imwrite('../../static/images/edited/canny/canny_3.png', canny_3)
    cv2.imwrite('../../static/images/edited/canny/canny_4.png', canny_4)

    

    
main()