import cv2
import numpy as np
import stacked_images
import gui_features

img1 = cv2.imread('imageSources/avengers.jpg')
img2 = cv2.imread('imageSources/balls.jpg')
img3 = cv2.imread('imageSources/car.jpg')
img4 = cv2.imread('imageSources/blue_ball.jpg')

cv2.namedWindow('extra',cv2.WINDOW_NORMAL)
#trackbars
def nothing(x):
    pass


def changing_colorspaces():
    '''
    print(len([i for i in dir(cv2) if i.startswith('COLOR')]))  totally 295  flags are there
    '''
    gray  = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    gray_img = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
    blank = np.zeros((1080,1080,3),np.uint8)

    stack = stacked_images.stacked_matrix([[img1,gray_img,hsv],[img1],[gray_img],[hsv,hsv,hsv,hsv]],0.3,(512,512),False)

    cv2.imshow('stack',stack)
    cv2.waitKey(0)

#changing_colorspaces()

def  thresholding():
    # rgb -> gray is converted into two types 1. gray = r+g+b/3   2. gray  = 0.3*r + 0.56*g + 0.block*b
    gray  = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    gray_img  = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)

    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(gray2, cv2.COLOR_GRAY2BGR)

    gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
    gray_img3 = cv2.cvtColor(gray3, cv2.COLOR_GRAY2BGR)

    gray4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
    gray_img4 = cv2.cvtColor(gray4, cv2.COLOR_GRAY2BGR)

    cv2.createTrackbar('thresh_val', 'extra', 0, 255, nothing)
    cv2.createTrackbar('maxval_val', 'extra', 0, 255, nothing)
    cv2.createTrackbar('block', 'extra', 3, 10, nothing)
    cv2.createTrackbar('const', 'extra', 0, 10, nothing)
    thresh_image = gray_img
    thresh_trunc=thresh_binary_inv=thresh_tozero=thresh_tozero_inv=thresh_adap_guassian=thresh_adap_mean = gray_img
    adaptive_guassian = adaptive_mean = gray_img
    adaptive_guassian2 = adaptive_mean2 = gray_img2
    adaptive_guassian3 = adaptive_mean3 = gray_img3
    adaptive_guassian4 = adaptive_mean4 = gray_img4
    cv2.namedWindow('extra',cv2.WINDOW_NORMAL)
    while True:
        #cv2.imshow('stacked_threshed_image',stacked_images.stacked_matrix([[thresh_image,img1,gray_img],[thresh_trunc,thresh_binary_inv,thresh_tozero],[thresh_tozero_inv,thresh_adap_guassian,thresh_adap_mean]],0.45))
        cv2.imshow('adaptive',stacked_images.stacked_matrix([[adaptive_guassian,adaptive_mean,img1,gray_img],\
                                                             [adaptive_guassian2,adaptive_mean2,img2,gray_img2],\
                                                             [adaptive_guassian3,adaptive_mean3,img3,gray_img3],\
                                                             [adaptive_guassian4,adaptive_mean4,img4,gray_img4] ],0.4,(512,512),True))
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        thresh = cv2.getTrackbarPos('thresh_val','extra')
        maxval  = cv2.getTrackbarPos('maxval_val','extra')
        block = cv2.getTrackbarPos('block','extra')
        constant = cv2.getTrackbarPos('const','extra')

        ret, thresh_image_b  = cv2.threshold(gray,thresh,maxval,cv2.THRESH_BINARY)
        thresh_image_b = cv2.cvtColor(thresh_image_b,cv2.COLOR_GRAY2BGR)

        ret, thresh_trunc = cv2.threshold(gray, thresh, maxval, cv2.THRESH_TRUNC)
        thresh_trunc = cv2.cvtColor(thresh_trunc, cv2.COLOR_GRAY2BGR)

        ret, thresh_binary_inv = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY_INV)
        thresh_binary_inv = cv2.cvtColor(thresh_binary_inv, cv2.COLOR_GRAY2BGR)

        ret, thresh_tozero = cv2.threshold(gray, thresh, maxval, cv2.THRESH_TOZERO)
        thresh_tozero = cv2.cvtColor(thresh_tozero, cv2.COLOR_GRAY2BGR)

        ret, thresh_tozero_inv = cv2.threshold(gray, thresh, maxval, cv2.THRESH_TOZERO_INV)
        thresh_tozero_inv = cv2.cvtColor(thresh_tozero_inv, cv2.COLOR_GRAY2BGR)

        ret, thresh_adap_guassian = cv2.threshold(gray, thresh, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
        thresh_adap_guassian = cv2.cvtColor(thresh_adap_guassian, cv2.COLOR_GRAY2BGR)

        ret, thresh_adap_mean = cv2.threshold(gray, thresh, maxval, cv2.ADAPTIVE_THRESH_MEAN_C)
        thresh_adap_mean = cv2.cvtColor(thresh_adap_mean, cv2.COLOR_GRAY2BGR)

        if block %2 == 1:

            adaptive_guassian  = cv2.adaptiveThreshold(gray,maxval,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,2)
            adaptive_guassian = cv2.cvtColor(adaptive_guassian,cv2.COLOR_GRAY2BGR)

            adaptive_mean = cv2.adaptiveThreshold(gray, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)
            adaptive_mean = cv2.cvtColor(adaptive_mean, cv2.COLOR_GRAY2BGR)

            adaptive_guassian2 = cv2.adaptiveThreshold(gray2, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5,2)
            adaptive_guassian2 = cv2.cvtColor(adaptive_guassian2, cv2.COLOR_GRAY2BGR)

            adaptive_mean2 = cv2.adaptiveThreshold(gray2, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)
            adaptive_mean2 = cv2.cvtColor(adaptive_mean2, cv2.COLOR_GRAY2BGR)

            adaptive_guassian3 = cv2.adaptiveThreshold(gray3, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5,2)
            adaptive_guassian3 = cv2.cvtColor(adaptive_guassian3, cv2.COLOR_GRAY2BGR)

            adaptive_mean3 = cv2.adaptiveThreshold(gray3, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)
            adaptive_mean3 = cv2.cvtColor(adaptive_mean3, cv2.COLOR_GRAY2BGR)

            adaptive_guassian4 = cv2.adaptiveThreshold(gray4, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5,2)
            adaptive_guassian4 = cv2.cvtColor(adaptive_guassian4, cv2.COLOR_GRAY2BGR)

            adaptive_mean4 = cv2.adaptiveThreshold(gray4, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)
            adaptive_mean4 = cv2.cvtColor(adaptive_mean4, cv2.COLOR_GRAY2BGR)


thresholding()

