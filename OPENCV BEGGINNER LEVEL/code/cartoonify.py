import cv2
import numpy as np
import sys
import stacked_images

original_image = cv2.imread('imageSources/pk.jpg')
cvt_original_image = cv2.cvtColor(original_image , cv2.COLOR_BGR2RGB)
gray_scaled_image =  cv2.cvtColor(cvt_original_image, cv2.COLOR_BGR2GRAY)
smoothed_image = cv2.medianBlur(gray_scaled_image , 13)

edged_image  = cv2.adaptiveThreshold(smoothed_image,175,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,19,3)
#edged_image = cv2.threshold(smoothed_image ,127,255, cv2.THRESH_TRUNC)
k = np.ones((5,5),np.uint8)
#edged_image = cv2.dilate(edged_image , k , 4)
color_image_1 = cv2.bilateralFilter(cvt_original_image,5,5,5,cv2.BORDER_DEFAULT)
color_image = cv2.bilateralFilter(original_image,5,5,5,cv2.BORDER_DEFAULT)
cartoon_image = cv2.bitwise_and(color_image , color_image , mask = edged_image)
cartoon_image_1 = cv2.bitwise_and(color_image_1 , color_image_1 , mask = edged_image)
if cvt_original_image is None:
    sys.exit()
#s = stacked_images.stacking_images([[original_image,gray_scaled_image,smoothed_image,edged_image],[color_image,cartoon_image,color_image_1,cartoon_image_1]],0.4,(900,700),True)
image_sized = stacked_images.stacking_images([[original_image,cartoon_image]],0.7,(1080,1080),True)
cv2.imshow('image',image_sized)
cv2.waitKey(0)
cv2.destroyAllWindows()