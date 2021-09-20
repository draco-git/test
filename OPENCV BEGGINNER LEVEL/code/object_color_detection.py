import cv2
import import_images
import stacked_images
import gui_features
import numpy as np

All_images  = import_images.dict_images()
img = All_images['all_colors1']
def void(x):
    pass
cv2.namedWindow('TRACKBAR')

cv2.createTrackbar('lH','TRACKBAR',0,179,void)
cv2.createTrackbar('lS','TRACKBAR',0,255,void)
cv2.createTrackbar('lV','TRACKBAR',0,255,void)
cv2.createTrackbar('hH','TRACKBAR',179,179,void)
cv2.createTrackbar('hS','TRACKBAR',255,255,void)
cv2.createTrackbar('hV','TRACKBAR',255,255,void)

hsv_image= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower = np.array([10,100,100])
upper = np.array([30,100,100])

#print(hsv_image.shape,single_colored_image.shape)

while True:
    lh = cv2.getTrackbarPos('lH','TRACKBAR')
    ls = cv2.getTrackbarPos('lS', 'TRACKBAR')
    lv = cv2.getTrackbarPos('lV', 'TRACKBAR')
    hh = cv2.getTrackbarPos('hH', 'TRACKBAR')
    hs = cv2.getTrackbarPos('hS', 'TRACKBAR')
    hv = cv2.getTrackbarPos('hV', 'TRACKBAR')
    lower = np.float32([lh,ls,lv])
    upper = np.float32([hh,hs,hv])

    single_colored_mask = cv2.inRange(hsv_image,lower,upper)

    colored_diagram = cv2.bitwise_and(img,img,mask=single_colored_mask)
    single_colored_mask = cv2.cvtColor(single_colored_mask, cv2.COLOR_GRAY2BGR)
    cv2.imshow('image',stacked_images.stacked_matrix([[img,single_colored_mask,colored_diagram]],0.3,(1080,980),False))
    if cv2.waitKey(100) & 0xFF==ord('s'):
        break
cv2.destroyAllWindows()