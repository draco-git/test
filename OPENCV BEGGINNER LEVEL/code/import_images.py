import os
import cv2
images =[]

def addimage(imagename):
    images.append(imagename)

for i in os.listdir('imageSources'):
    images.append(i)

s=dict()


for i in images:
    a = (i.split('.'))[0]
    s[a] = str('imageSources\\'+i)

def show():
    print('the images in directory are', [i for i, j in s.items()])
    return True

def extract(image):
    for i,j in s.items():

        if i==image:
            return ('imageSources\\'+j)

def allImages():
    return [ str('imageSources\\'+i) for i in images]

def dict_images():#dict of images
    for i,j in s.items():
        s[i] = cv2.imread(j)
    return s

#print(dict_images())