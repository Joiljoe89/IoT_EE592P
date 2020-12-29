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
    
    #blue - calculate the histogram
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
    
    histb = np.histogram(blue,bins=256)
    hb=histb[0]
    fvb1 = [[0,0,0,0,0,0,0,0]]
    for i in range(0,(hb.shape[0]),8):
        fvb = hb[i:i+8]
        fvb1 = [fvb] + fvb1
    np.savetxt('/home/pi/Desktop/iot_project/project_data/iot_data/west/training/cloudy_fv8/fvb%s.txt' %im[0:24], fvb1, fmt='%.2e')
    fvb1 = [[0,0,0,0,0,0,0,0]]

    #green - calculate the histogram
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

    histg = np.histogram(green,bins=256)
    hg=histg[0]
          
    fvg1 = [[0,0,0,0,0,0,0,0]]
    for i in range(0,(hg.shape[0]),8):
        fvg = hg[i:i+8]
        fvg1 = [fvg] + fvg1
    np.savetxt('/home/pi/Desktop/iot_project/project_data/iot_data/west/training/cloudy_fv8/fvg%s.txt' %im[0:24], fvg1, fmt='%.2e')
    fvg1 = [[0,0,0,0,0,0,0,0]]

    #red - calculate the histogram
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

    histr = np.histogram(red,bins=256)
    hr=histr[0]
        
    fvr1 = [[0,0,0,0,0,0,0,0]]
    for i in range(0,(hr.shape[0]),8):
        fvr = hr[i:i+8]
        fvr1 = [fvr] + fvr1
    np.savetxt('/home/pi/Desktop/iot_project/project_data/iot_data/west/training/cloudy_fv8/fvr%s.txt' %im[0:24], fvr1, fmt='%.2e')
    fvr1 = [[0,0,0,0,0,0,0,0]]