# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:31:06 2018

@author: joe
"""
import time
import cv2
import numpy as np
#from sklearn.feature_extraction import image
from PIL import Image
#path = 'D:/Seafile/Seafile/My Library/IIT Mandi/even_course_feb18/EE592P_IoT/assignment/pi/west_picamera_pics/west_img2018-05-16-14-35.jpg'
path = '/home/pi/Desktop/iot project/east data/east_img2018-05-15-05-38.jpg'
#path = '/home/pi/Desktop/iot project/date/img/north_img2018-05-23-01-22.jpg'
img = cv2.imread(path)

'''
original=Image.open(path)
print(original.format,original.size,original.mode)
original.show()
[col,row]=(original.size)
'''
#split to RGB
blue, green, red = cv2.split(img)
row = img.shape[0]
col = img.shape[1]

# Define the window size
windowsize_r = 18
windowsize_c = 24
'''
# Crop out the window and calculate the histogram
for r in range(0,row - windowsize_r, windowsize_r):
    for c in range(0,col - windowsize_c, windowsize_c):
        window = img[r:r+windowsize_r,c:c+windowsize_c]
        hist = np.histogram(window,bins=256)
'''
#blue - Crop out the window and calculate the histogram
hb1 = ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0])
for r in range(0,(row+windowsize_r) - windowsize_r, windowsize_r):
    for c in range(0,(col+windowsize_c) - windowsize_c, windowsize_c):
        window = blue[r:r+windowsize_r,c:c+windowsize_c]
        histb = np.histogram(window,bins=256)
        hb=histb[0]
        hb1=np.concatenate((hb,hb1),axis=0)
        #print(hr1)
        #cv2.imwrite('sample_patch%s%s.jpg' %(r,c) ,window)
fvb1 = [[0,0,0,0,0,0,0,0]]
for i in range(0,(hb1.shape[0]-256),8):
    fvb = hb1(i:i+8)
    fvb1 = [fvb] + fvb1
        
        
#green - Crop out the window and calculate the histogram
hg1 = ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0])
for r in range(0,(row+windowsize_r) - windowsize_r, windowsize_r):
    for c in range(0,(col+windowsize_c) - windowsize_c, windowsize_c):
        window = green[r:r+windowsize_r,c:c+windowsize_c]
        histg = np.histogram(window,bins=256)
        hg=histg[0]
        hg1=np.concatenate((hg,hg1),axis=0)
        #print(hg1)
        #cv2.imwrite('sample_patch%s%s.jpg' %(r,c) ,window)
fvg1 = [[0,0,0,0,0,0,0,0]]
for i in range(0,(hg1.shape[0]-256),8):
    fvg = hg1(i:i+8)
    fvg1 = [fvg] + fvg1
#red - Crop out the window and calculate the histogram
#hr1=np.ones((1,8))
hr1 = ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0])
for r in range(0,(row+windowsize_r) - windowsize_r, windowsize_r):
    for c in range(0,(col+windowsize_c) - windowsize_c, windowsize_c):
        window = red[r:r+windowsize_r,c:c+windowsize_c]
        histr = np.histogram(window,bins=256)
        hr=histr[0]
        hr1=np.concatenate((hr,hr1),axis=0)
        print(hr1)
        #cv2.imwrite('sample_patch%s%s.jpg' %(r,c) ,window)
fvr1 = [[0,0,0,0,0,0,0,0]]
for i in range(0,(hr1.shape[0]-256),8):
    fvr = hr1(i:i+8)
    fvr1 = [fvr] + fvr1
#############################################################################
  

'''
#######################
#patches = image.extract_patches_2d(original, (24, 18))
#print(patches.shape)
#patches[0]
#########################

#hist=np.histogram(original,bins=256)
#print(hist)
'''