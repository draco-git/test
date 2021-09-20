import cv2
import stacked_images as stack
import gui_features
img = cv2.imread('imageSources/shapes_color.jpg')
# l = stack.stacking_images([[img]],0.5,(1080,950),False)
def harris_corner_detection(img):
    gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    dst1 = cv2.cornerHarris(gray_img, 4, 11, 0.04)
    # result is dilated for marking the corners, not important
    dst = cv2.dilate(dst1, None,iterations=5)
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst > 0.01 * dst1.max()] = [0, 0, 255]
    k = stack.stacking_images([[dst,dst1]],0.5,(1080,950),True)
    l = stack.stacking_images([[img ]],0.5,(1090,950),True)
    gui_features.finding_bgr(l,'image')

# harris_corner_detection(img)
hand = cv2.imread('imageSources/hand_detection/hand1.jpg')
l = stack.stacking_images([[hand ]],0.5,(1090,950),True)
gui_features.finding_bgr(l,'image')
def contours(img):
    gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    thresh_img = cv2.threshold(gray_img , )
    pass