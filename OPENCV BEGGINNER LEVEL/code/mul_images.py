import cv2
import os

# for multiple images
ipath = 'imageSources'
def mul():
    for i in os.listdir(ipath):
        q=os.path.join(ipath+'\\',i)
        img = cv2.imread(q,0)
        smallimg = cv2.resize(img,None,fx=1/2,fy=1/2,interpolation=cv2.INTER_AREA)
        cv2.imshow(q+'wind',smallimg)
    if cv2.waitKey(0) & 0xFF  == ord('s'):
        cv2.destroyAllWindows()
#********************************************************************************************************/

