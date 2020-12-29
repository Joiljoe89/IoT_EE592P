# -*- coding: utf-8 -*-
"""
Created on Tue May 29 09:13:19 2018

@author: Joe Johnson
class=cloudy
"""

import cv2
import numpy as np
import os,os.path

path = '/home/pi/Desktop/iot_project/project_data/iot_data/west/training/cloudy'
list_files = os.listdir(path)
for im in list_files:

    img = cv2.imread(path+'/'+im)
    
    #split to RGB
    blue, green, red = cv2.split(img)
    row = img.shape[0]
    col = img.shape[1]
    
    # Define the window size
    windowsize_r = 18
    windowsize_c = 24
    
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
        fvb = hb1[i:i+8]
        fvb1 = [fvb] + fvb1
    np.savetxt('/home/pi/Desktop/iot_project/project_data/iot_data/west/training/cloudy_fv8/fvb%s.txt' %im[0:24], fvb1, fmt='%.2e')
    fvb1 = [[0,0,0,0,0,0,0,0]]

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
        fvg = hg1[i:i+8]
        fvg1 = [fvg] + fvg1
    np.savetxt('/home/pi/Desktop/iot_project/project_data/iot_data/west/training/cloudy_fv8/fvg%s.txt' %im[0:24], fvg1, fmt='%.2e')
    fvg1 = [[0,0,0,0,0,0,0,0]]

    #red - Crop out the window and calculate the histogram
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
        fvr = hr1[i:i+8]
        fvr1 = [fvr] + fvr1
    np.savetxt('/home/pi/Desktop/iot_project/project_data/iot_data/west/training/cloudy_fv8/fvr%s.txt' %im[0:24], fvr1, fmt='%.2e')
    fvr1 = [[0,0,0,0,0,0,0,0]]