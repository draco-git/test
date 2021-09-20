import cv2
import numpy as np
import import_images
import stacked_images
import gui_features

#reading images

images = import_images.dict_images()
names_of_img_in_dict =[ ]
for i,j in images.items():
    images[i] = cv2.imread(j)
    names_of_img_in_dict.append(i)

#print(names_of_img_in_dict) : ['avengers', 'balls', 'black_ball', 'blue_ball', 'buildings', 'car', 'dragon', 'iphone_logo', 'logo']
#images dict consists of all read images

#geomatric transformations

#.Translation : transformation matrix req is [[1 0 tx],[0,1,ty]]

def translation():
    img = images['car']
    transformation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
    r, c, ch = img.shape
    trans_img = cv2.warpAffine(img, transformation_matrix, (r, c))
    cv2.imshow('trans_img', stacked_images.stacked_matrix([[trans_img, img]], 0.9,(512,512),False))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#translation()

#rotation: transformation_matrix req is obtained by cv2.getRotationMatrix2D((cols,rows),angle,scale)

def rotaion():
    img = images['buildings']
    img = cv2.resize(img,(512,512))
    M = cv2.getRotationMatrix2D((256,256),45,0.5) # here 0.5 is the scale in which the output image is showed
    rot_img = cv2.warpAffine(img,M,(512,512))
    cv2.imshow('rotate_img',stacked_images.stacked_matrix([[img,rot_img]],1,(512,512),False))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#rotaion()

#Affine transformation : here in the output image the lines are parallel similar to input image
#in this we cv2.getAffineTransform() to give transformation_matrix

def affine_transform():
    out = np.ones((512,512,3),np.uint8)
    img = images['buildings']
    img  = cv2.resize(img,(512,512))
    r,c,ch = img.shape
    points = gui_features.finding_bgr(img)
    output_img = cv2.resize(out,(r,c))
    out_points = gui_features.finding_bgr(output_img)
    print(points,out_points)
    M = cv2.getAffineTransform(np.float32([points]),np.float32([out_points]))
    print(M)
    dst  = cv2.warpAffine(img,M,(r,c))
    cv2.imshow('ouput',stacked_images.stacked_matrix([[img,dst]],1,(512,512),False))
    cv2.waitKey(0)

#affine_transform()

#perspective_transformation : here we use cv2.getPerspectiveTransforms()

def perspective_transform():
    out  = np.ones((512,512,3),np.uint8)
    img = images['cards']
    img = cv2.resize(img,(512,512))
    points = gui_features.finding_bgr(img)
    input_points = np.float32([points])
    out_image = cv2.resize(out,(img.shape[0],img.shape[1]))
    o_points = gui_features.finding_bgr(out_image)
    output_points = np.float32([o_points])
    M = cv2.getPerspectiveTransform(input_points,output_points)
    dst = cv2.warpPerspective(img,M,(img.shape[0],img.shape[1]))
    cv2.imshow('output',stacked_images.stacked_matrix([[img,dst]],0.8,(512,512),False))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#perspective_transform()

#blurring images

def nothing(x): # function used for trackbar
    pass

def blurring():

    img = images['black_ball']
    while True:
        kernel = int(input('enter kernel value'))
        if kernel == 0:
            break
        guassian_blur = cv2.GaussianBlur(img, (kernel,kernel), 0)
        median_blur = cv2.medianBlur(img, kernel) # median_blur makaes the most blurred compared to guassian_blur
        bilteral_filter_image  =  cv2.bilateralFilter(img,11,11,11,cv2.BORDER_DEFAULT)  # only used for noise removal and effective

        cv2.imshow('images_blurred', stacked_images.stacked_matrix([[img, guassian_blur, median_blur,bilteral_filter_image]], 0.5,(512,512),False))
        if cv2.waitKey(0) & 0xFF == ord('s'):
            cv2.destroyAllWindows()

#blurring()

# morphological transformations : normally performed on binary images , consist of two methods erosion and dilution.

# erosion:

def morpho_transformations():

    img = images['cards']
    gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    while True:
        kernel = int(input('enter kernel'))
        if kernel == 0:
            break
        #iterations = int(input('enter no of iterations'))

        k = np.ones((kernel,kernel),np.uint8)
        dilate  = cv2.dilate(gray_image,k,iterations)
        erode = cv2.erode(gray_image,k,iterations)
        opening = cv2.morphologyEx(gray_image,cv2.MORPH_OPEN,k)
        closing = cv2.morphologyEx(gray_image, cv2.MORPH_CLOSE, k)
        morphology_gradient = cv2.morphologyEx(gray_image,cv2.MORPH_GRADIENT,k)
        top_hat = cv2.morphologyEx(gray_image,cv2.MORPH_TOPHAT,k)
        black_hat = cv2.morphologyEx(gray_image,cv2.MORPH_BLACKHAT,k)


        cv2.imshow('morpho_transformations',stacked_images.stacked_matrix([[opening,closing,morphology_gradient],[top_hat,black_hat]],0.5,(512,512),True))
        if cv2.waitKey(0) & 0xFF == ord('s'):
            cv2.destroyAllWindows()
#morpho_transformations()


