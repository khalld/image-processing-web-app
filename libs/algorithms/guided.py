# from cv2.ximgproc import guidedFilter
import numpy as np
import cv2


def main():
    print("hello world")

    path = '../../static/images/'

#     img = Image.open(path + 'test.png').convert('L')

    img = cv2.imread(path + 'test.png')    
    # guided = cv2.GuidedFilter(img,13,70)    
    cv2.imshow("image",img)    
    # cv2.imshow("guided filtering",guided)    
    cv2.waitKey()

main()