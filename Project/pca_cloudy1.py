# -*- coding: utf-8 -*-
"""
Created on Tue May 29 09:22:55 2018

@author: Joe Johnson

class=sunny
PCA, 8D->2D
"""
import numpy as np
import os,os.path
from sklearn.decomposition import PCA

path_fv = 'C:/Users/Pinnacle/Desktop/iot_data/west/training/cloudy_f8/'
list_files1 = os.listdir(path_fv)
for fv in list_files1:
    
    fv_pca = [0]
    X=[[0,0,0,0,0,0,0,0]]
    f = open(path_fv+fv,'r')
    f1 = f.readlines()
    for x in f1:
        print(x)
        x = x[0:(len(x)-1)]
        a = int(len(x)/8)
        x1 = x[0:a]
        x2 = x[a:(2*a+1)]
        x3 = x[(2*a+1):(3*a+2)]
        x4 = x[(3*a+2):(4*a+3)]
        x5 = x[(4*a+3):(5*a+4)]
        x6 = x[(5*a+5):(6*a+6)]
        x7 = x[(6*a+6):(7*a+7)]
        x8 = x[(7*a+7):(8*a+7)]
    
        x = (float(x1), float(x2),float(x3), float(x4),float(x5), float(x6),float(x7), float(x8))
        x = list(x)
        X=[x[0:8]]+X
        
    X=X[0:(len(X)-1)]
    
    pca = PCA(n_components=1)
    pca.fit(X)
    X_pca = pca.transform(X)
    print("transformed shape:", X_pca.shape)
    for i in range(0,X_pca.shape[0]):
        fv_pca = np.concatenate((fv_pca,X_pca[i]),axis=0)
        #a = ' '
        #fv_pca = float('%d%s%d' %(fv_pca,a,X_pca[0]))
    np.savetxt('C:/Users/Pinnacle/Desktop/iot_data/west/training/cloudyfv2/fv%s.txt' %fv[0:27], fv_pca[1:], fmt='%.2e')
#############################################################################