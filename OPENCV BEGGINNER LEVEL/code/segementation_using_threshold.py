import cv2
import random as rd
import import_images  # dict_images
import stacked_images  # stacking_matrix
import gui_features  # finding_bgr

all_images = import_images.dict_images()
img = all_images['black_ball']
new_gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def nothing(x):
    pass


cv2.namedWindow('trackbar')
random_value  =  rd.randint(0,255)
print(random_value)
cv2.createTrackbar('thresh', 'trackbar', rd.randint(0,255), 255, nothing)
cv2.createTrackbar('maxval', 'trackbar', rd.randint(0,255), 255, nothing)

binary_thresh = inv_binary_thresh = trunc = tozero_thresh = inv_tozero_thresh = new_gray_img

while True:
    imgg = stacked_images.stacked_matrix([[binary_thresh, inv_binary_thresh], [tozero_thresh, inv_tozero_thresh], [trunc]],
                                  0.5, (512, 512), True)
    cv2.imshow('thresh', imgg)

    if cv2.waitKey(100) & 0xFF == ord('s'):
        break

    thresh = cv2.getTrackbarPos('thresh', 'trackbar')
    maxval = cv2.getTrackbarPos('maxval', 'trackbar')

    ret,binary_thresh = cv2.threshold(new_gray_img, thresh, maxval, cv2.THRESH_BINARY)
    ret,inv_binary_thresh = cv2.threshold(new_gray_img, thresh, maxval, cv2.THRESH_BINARY_INV)
    ret,trunc = cv2.threshold(new_gray_img, thresh, maxval, cv2.THRESH_TRUNC)
    ret,tozero_thresh = cv2.threshold(new_gray_img, thresh, maxval, cv2.THRESH_TOZERO)
    ret,inv_tozero_thresh = cv2.threshold(new_gray_img, thresh, maxval, cv2.THRESH_TOZERO_INV)


print('points',gui_features.finding_bgr(imgg))

cv2.destroyAllWindows()
