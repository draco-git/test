import cv2
import mul_images
import numpy as np
import import_images as ii


def shapes():
    white_image = np.ones((512, 512, 3))  # 1->white and 0->black
    # shapes
    color = (0, 0, 0)  # bgr in opencv
    cv2.rectangle(white_image, (0, 0), (512, 512), color, 5)
    cv2.circle(white_image, (256, 256), 100, (255, 0, 0), 5)
    cv2.circle(white_image, (256, 256), 50, (255, 0, 0), -1)  # if thickness is -1 then it will the color
    cv2.line(white_image, (156, 256), (356, 256), (0, 0, 255), 5)
    polygon_points = np.array([(0, 256), (256, 156), (512, 256), (256, 356)],
                              np.int32)  # these are vertices of the polygon and these must be in form of int32
    polygon_points = polygon_points.reshape(
        (-1, 1, 2))  # after change the shape into ROWS*1*2 and in reshape(-1)->flattening of array
    cv2.polylines(white_image, [polygon_points], True, color, 5)  # true is for ->isClosed argument

    # text
    cv2.putText(white_image, 'madhav', (125, 400), cv2.FONT_ITALIC, 2, (0, 255, 0), 3)

    cv2.imshow('white', white_image)
    cv2.waitKey(0)

'''
cv2.namedWindow('blackwindow',cv2.WINDOW_NORMAL)# there are totally 6 flages normal,auto_size,gui_normal,gui_expanded,fullscreen,keepratio,freeratio,opengl
    cv2.resizeWindow('blackwindow',512,512)#to resize the window
'''

def empty(x):
    pass

def trackbar():
    cv2.namedWindow('trackbars')#window to hold trackbars
    #creating trcakbars
    cv2.createTrackbar('blue','trackbars',0,255,empty)
    cv2.createTrackbar('green', 'trackbars', 0, 255, empty)
    cv2.createTrackbar('red', 'trackbars', 0, 255, empty)

    black = np.zeros((512, 512, 3), np.uint8)
    while True:

        cv2.imshow('trackbars', black)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        # here b,g,r has the value of trackbars at instant
        b = cv2.getTrackbarPos('blue', 'trackbars')
        g = cv2.getTrackbarPos('green', 'trackbars')
        r = cv2.getTrackbarPos('red', 'trackbars')
        black[:] = [b,g,r]


    cv2.destroyAllWindows()

img  = cv2.imread('imageSources/black_ball.jpg')
image  = cv2.resize(img,(512,512))

def click_mouse(event,x,y,flags,param):
    points = []
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('x and y coordinates')
        print('x =',x,'y =',y)
        print('bgr values at'+'('+str(x)+','+str(y)+')','=',image[x,y])
        cv2.circle(image,(x,y),2,(0,0,255),-1)
        points.append((x,y))
    if event == cv2.EVENT_RBUTTONDBLCLK  and len(points)>2:
        poly_points  = np.array(points,np.int32)
        poly_points = poly_points.reshape((-1,1,2))
        cv2.polylines(image,poly_points,True,(0,255,0),2)

def paint_brush():

    '''
    print([i for i in dir(cv2) if 'EVENT' in i])
    ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON',
    'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN',
    'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
    '''
#learning mouse events in opencv. Possible through setMouseCallback() method

    cv2.namedWindow('paint_brush_window')
    cv2.setMouseCallback('paint_brush_window',click_mouse)

    while True:
        cv2.imshow('paint_brush_window',image)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    cv2.destroyAllWindows()

#paint_brush()





def finding_bgr_single_image(image,winName):
    def bgr(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            #cv2.circle(image, (x, y), 2, (0, 0, 255), -1)
            print(image.shape)
            print(winName+'[' + str(x) + ',' + str(y) + ']', image[y,x])
            points.append((x, y))

    points =[]
    cv2.namedWindow(winName)
    cv2.setMouseCallback(winName,bgr)
    image = cv2.resize(image,(512,512))
    cv2.imshow(winName,image)
    return points

def finding_bgr(image,winName):
    def bgr(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            #cv2.circle(image, (x, y), 2, (0, 0, 255), -1)

            print(winName+'[' + str(x) + ',' + str(y) + ']', image[y,x])
            points.append((x, y))

    points =[]
    cv2.namedWindow(winName)
    cv2.setMouseCallback(winName,bgr)
    # print(image.shape)

    cv2.imshow(winName , image)
    if cv2.waitKey(0) & 0xff == 's':
        cv2.destroyAllWindows()
    return points

