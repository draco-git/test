import cv2
import numpy as np
import import_images
from matplotlib import pyplot as plt
import stacked_images
import gui_features


images_dict = import_images.dict_images()


#histogram ; it is frequency of pixels in gray_scale_image i.e ranging from 0 to 255.

def histogram():
    img = images_dict['avengers']
    gray_img  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray_img,cv2.COLOR_GRAY2BGR)

    img_histr = cv2.calcHist([gray],[0],None,[256],[0,256])
    img_equ = cv2.equalizeHist(gray_img)
    cv2.imshow('hist',stacked_images.stacked_matrix([[gray_img,img_equ]],0.8,(512,512),True))
    cv2.waitKey(0)
    plt.plot(img_histr)
    plt.plot(img_equ)
    plt.show()


#histogram()

#image gradients

#canny edge detection
def nothing(x):
    pass

def canny():

    img = images_dict['avengers']
    gray_img  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('trackbar')
    cv2.createTrackbar('low_thresh','trackbar',0,255,nothing)
    cv2.createTrackbar('high_thresh','trackbar',255,255,nothing)
    while True:

        thresh1 = cv2.getTrackbarPos('low_thresh','trackbar')
        thresh2  = cv2.getTrackbarPos('high_thresh','trackbar')
        canny_img = cv2.Canny(gray_img,thresh1,thresh2)
        points = stacked_images.stacked_matrix_image_map([[canny_img,gray_img],[gray_img]],0.5,(1080,720),True,'canny_imag')
        k = cv2.waitKey(10) & 0xFF
        if k == ord('s'):
            break

    cv2.destroyAllWindows()
#canny()

#countours : curve joined all the continous points having same colr and intensity.

def find_draw_contors():
     img = images_dict['avengers']
     gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     edged_img = cv2.Canny(img,127,215)
     edged_img2 = cv2.cvtColor(edged_img,cv2.COLOR_GRAY2BGR)
     gray_points = gui_features.finding_bgr_single_image(gray_img,'gray_image')

     contour_points,heirarchy = cv2.findContours(edged_img,1,2)

     cv2.drawContours(img,contour_points,-1,(0,255,0),2)
     stacked_images.stacked_matrix_image_map([[edged_img2,img]],1,(512,512),False,'find_countours')
     cv2.waitKey(0)
     cv2.destroyAllWindows()
#find_draw_contors()



