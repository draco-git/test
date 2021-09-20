import cv2
import stacked_images
import numpy as np

def motion_detection(video,k,frame_rate,dim,is_erode):
    cap = cv2.VideoCapture(video)

    ret1,frame1 = cap.read()
    ret2,frame2 = cap.read()
    kernel = np.ones((k,k),np.uint8)
    while cap.isOpened():
        blank = np.zeros((dim[1], dim[0], 3), np.uint8)
        try:
            diff = cv2.absdiff(frame1,frame2)
        except:
            break
        gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        gray_img = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
        blur = cv2.GaussianBlur(gray, (7, 7), 1)
        blur_img = cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)
        r,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
        thresh_img = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)
        canny = cv2.Canny(gray_img,20,255)
        canny_img = cv2.cvtColor(canny,cv2.COLOR_GRAY2BGR)

        morph = cv2.dilate(thresh, kernel, iterations=1)
        contours,heirarchy = cv2.findContours(morph,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #print(len(contours))
        hull =  []
        for i in contours:
            hull.append(cv2.convexHull(i))
        '''for i in contours:
            if cv2.contourArea(i) < 4000:
                continue
            (x,y,w,h) = cv2.boundingRect(i)
            cv2.rectangle(duplicate,(x,y),(x+w,y+h),(0,255,0),2)'''
        cv2.drawContours(frame1, contours, -1, (255, 255, 0), 2, lineType=cv2.CONTOURS_MATCH_I3)
        cv2.drawContours(blank, contours, -1, (255,255,255), 2, lineType=cv2.CONTOURS_MATCH_I3)
        stacked_images.stacked_matrix_image_map([[frame1,blank,gray_img,canny_img],[thresh_img,blur_img,diff]],0.5,dim,False,'feed')
        if cv2.waitKey(frame_rate) & 0xFF == ord('s'):
            break
        frame1 = frame2
        ret3,frame2 = cap.read()


    cap.release()
    cv2.destroyAllWindows()
motion_detection('videoSources/shinchan.gif',5,frame_rate=200,dim = (512,512),is_erode=True)