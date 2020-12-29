# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:04:01 2018

@author: Joe Johnson,
SVM, kernel=rbf, classify=sunny,cloudy,night
"""

import pandas as pd
#lib for analysis
import numpy as np
from sklearn import svm

#read training data
tr_all_class = pd.read_csv('C:/Users/Pinnacle/Desktop/iot_data/west/west_temp_humd.csv',delimiter=',')

classes = tr_all_class[['t','h']].as_matrix()
c1 = np.zeros(11)
c2 = np.ones(13)
c3 = 2*np.ones(16)
type_label = np.concatenate((c1,c2,c3),axis=0)

#Fit the model
#model = svm.SVC(kernel='linear',C=1)
#model = svm.SVC(kernel='poly', C=1, gamma=1.54, degree=5)
#model = svm.SVC(kernel='linear',decision_function_shape='ovr')#one vs rest
#model = svm.SVC(kernel='linear',decision_function_shape='ovo')#one vs one
model = svm.SVC(kernel='rbf', C=1, gamma=1)#radial basis function
model.fit(classes, type_label)

x_ts = 43
y_ts = 20


if(model.predict([[x_ts, y_ts]]))==0:
    print('belong to class = sunny!!')
        
elif(model.predict([[x_ts, y_ts]]))==1:
    print('belong to class = cloudy!!')
        
else:
    print('belong to class = night!')
       