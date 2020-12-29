# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:31:06 2018

@author: joe
"""

import cv2
import numpy as np
#from sklearn.feature_extraction import image
from PIL import Image
#path = 'D:/Seafile/Seafile/My Library/IIT Mandi/even_course_feb18/EE592P_IoT/assignment/pi/west_picamera_pics/west_img2018-05-16-14-35.jpg'
#path = '/home/pi/Desktop/iot project/east data/east_img2018-05-15-05-38.jpg'
path = '/home/pi/Desktop/iot project/date/img/north_img2018-05-23-01-22.jpg'
img = cv2.imread(path)

'''
original=Image.open(path)
print(original.format,original.size,original.mode)
original.show()
[col,row]=(original.size)
'''
#split to RGB
b, g, r = cv2.split(img)

# Define the window size
windowsize_r = 18
windowsize_c = 24

# Crop out the window and calculate the histogram
for r in range(0,test_image.shape[0] - windowsize_r, windowsize_r):
    for c in range(0,test_image.shape[1] - windowsize_c, windowsize_c):
        window = test_image[r:r+windowsize_r,c:c+windowsize_c]
        hist = numpy.histogram(window,bins=grey_levels)

########################
#patches = image.extract_patches_2d(original, (24, 18))
#print(patches.shape)
#patches[0]
#########################

hist=np.histogram(original,bins=256)
#print(hist)