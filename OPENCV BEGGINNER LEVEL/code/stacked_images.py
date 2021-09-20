import cv2
import numpy as np
import gui_features




def stacking(imgArray,matrix,scale):
    if isinstance(imgArray) != list:
        imageMatrix = imgArray.reshape((matrix[1],matrix[0]))
        imgArrays = [cv2.imread(i) for i in imgArray]
        min_dim  = min([i.shape for i in imgArrays])
        max_dim = max([i.shape for i in imgArrays])
        avg_dim = (sum([(i.shape[0]) for i in imgArrays])//len(imgArrays),sum([(i.shape[1]) for i in imgArrays])//len(imgArrays))
        print([i.shape for i in imgArrays])
        print('min',min_dim,'max',max_dim,'avg',avg_dim)
        same_size_imgArrays = [cv2.resize(i,(1080,720)) for i in imgArrays]
        imgArrays = [cv2.resize(i,(0,0),None,scale,scale) for i in same_size_imgArrays]
        n = matrix[1]
        image_arrays=[]
        for i in range(0,len(imgArrays),n):
            image_arrays.append(imgArrays[i:i+n])
        img = cv2.vconcat([cv2.hconcat(list_h) for list_h in image_arrays])
        cv2.imshow('image_stacked',img)
        cv2.waitKey(0)
    else:
        print('use stacking_matric function')


def stacked_matrix(image_matrix, scale,new_dim,isAllGray): # isAllGray means all images are gray images
    sized_image_matrix = []  # 1 Used to store same_sized_images i.e. storing images having same dimensions.
    resized_im = []  # used to store images of same-sized_images after using scaling them.
    max_len =max([len(i) for i in image_matrix])

    for i in image_matrix:
        if len(i) == max_len and i not in sized_image_matrix:
            sized_image_matrix.append([cv2.resize(k, new_dim) for k in i])
        elif i not in sized_image_matrix:
            n = max_len-len(i)
            for count in range(n):
                if isAllGray:
                    i.append(np.zeros((512,512),np.uint8))
                else:
                    i.append(np.zeros((512,512,3),np.uint8))
            #print(len(i))
            sized_image_matrix.append([cv2.resize(k, new_dim) for k in i])

    for j in sized_image_matrix:
        resized_im.append([cv2.resize(k, None, (0, 0), scale, scale) for k in j])  # 2

    stacked_matrix = cv2.vconcat([cv2.hconcat(list_h) for list_h in resized_im])
    #points = gui_features.finding_bgr(stacked_matrix,winName)
    return stacked_matrix

def stacked_matrix_image_map(image_matrix, scale,new_dim,isAllGray,winName): # isAllGray means all images are gray images

    sized_image_matrix = []  # 1 Used to store same_sized_images i.e. storing images having same dimensions.
    resized_im = []  # used to store images of same-sized_images after using scaling them.
    max_len =max([len(i) for i in image_matrix])
    for i in image_matrix:
        print(i,i.shape)
        if len(i) == max_len and i not in sized_image_matrix:
            sized_image_matrix.append([cv2.resize(j, new_dim) for j in i])
        elif i not in sized_image_matrix:
            n = max_len-len(i)
            for count in range(n):
                if isAllGray:
                    i.append(np.zeros((512,512),np.uint8))
                else:
                    i.append(np.zeros((512,512,3),np.uint8))
            #print(len(i))
            sized_image_matrix.append([cv2.resize(j, new_dim) for j in i])

    for j in sized_image_matrix:
        resized_im.append([cv2.resize(k, None, (0, 0), scale, scale) for k in j])  # 2

    stacked_matrix = cv2.vconcat([cv2.hconcat(list_h) for list_h in resized_im])
    points = gui_features.finding_bgr(stacked_matrix,winName)
    return points


#cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)


def stacking_images(matrix_images , scale , new_dim , isColor):
    same_size_images = []
    same_scaled_images = []
    stack_len = max([len(i) for i in matrix_images])

    for i in matrix_images:
        if len(i) == stack_len:
            hash = []
            for j in i:
                if j.ndim == 2:
                    j = cv2.cvtColor(j , cv2.COLOR_GRAY2BGR)
                print(j.ndim, j.shape)
                hash.append(cv2.resize(j, new_dim))
            same_size_images.append(hash)
        else:
            n = stack_len - len(i)
            hash = []
            for j in i:
                print(j)
                if j.ndim == 2 and isColor:
                    j = cv2.cvtColor(j , cv2.COLOR_GRAY2BGR)
                hash.append(cv2.resize(j, new_dim))
            for k in range(n):
                print('k',k)
                if isColor:
                    print('iscolor')
                    hash.append(cv2.resize(np.zeros((512,512,3),np.uint8),(new_dim)))
                else:
                    hash.append(cv2.resize(np.zeros((512,512),np.uint8),(new_dim)))

            print('iscolor',len(hash))
            same_size_images.append(hash)

    for j in same_size_images:
        same_scaled_images.append([cv2.resize(k, None,(0,0), scale, scale) for k in j])  # 2
    for k in same_scaled_images:
        for j in k:
            print(j.shape)
    stacked_matrix = cv2.vconcat([cv2.hconcat(list_h) for list_h in same_scaled_images])
    return stacked_matrix

# imggg = cv2.imread('imageSources/car.jpg')
# im = cv2.cvtColor(imggg , cv2.COLOR_BGR2GRAY)
# a = stacking_images([[imggg , im]],0.3,(1080,980),True)
# cv2.imshow('stacking images',a)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#stacking(imgArray,[3,3],0.2)
'''
img = imgArray[0]

image = cv2.imread(img)
image  = cv2.resize(image,(256,256))
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray  = cv2.cvtColor(gray_image,cv2.COLOR_GRAY2BGR)
im = cv2.hconcat([image,gray])
cv2.imshow('stack',im)
cv2.waitKey(0)

'''