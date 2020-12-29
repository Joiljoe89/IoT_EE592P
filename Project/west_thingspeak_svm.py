# -*- coding: utf-8 -*-
"""
Created on Wed May 30 16:26:37 2018

@author: Joe Johnson
ds18b20,HAT,SVM
"""
import time

from sklearn import svm
import numpy as np
import pandas as pd
from time import gmtime, strftime
import serial
from sense_hat import SenseHat
sense = SenseHat()
bg_exit=[0,0,0]

import urllib3
proxy = urllib3.ProxyManager('https://10.8.0.1:8080/')

try:
    while True:
        ser=serial.Serial("/dev/ttyACM0",9600)
        ser.baudrate=9600
        ####################
        read_ser=ser.readline()
        t1 = read_ser
        t1 = t1[0:4]
        t1 = float(t1)
        ###################
        t= sense.get_temperature()
        p= sense.get_pressure()
        h= sense.get_humidity()
                        
        t2= round(t,1)
                        
        p1= round(p,1)
        #print(p1)
        h1= round(h,1)
                            
        if t1>=20.0 and t1<35.0:
            bg=[0,100,0]
        else:
            if t1<20.0:
                bg=[0,0,100]
            else:
                bg=[100,0,0]
        
        ####################################
        #read training data
        tr_all_class = pd.read_csv('/home/pi/Desktop/iot_west_pics/west_temp_humd.csv',delimiter=',')
        
        classes = tr_all_class[['t','h']].as_matrix()
        c1 = np.zeros(11)
        c2 = np.ones(29)
        type_label = np.concatenate((c1,c2),axis=0)
        
        #Fit the model
        #model = svm.SVC(kernel='linear',C=1)
        #model = svm.SVC(kernel='poly', C=1, gamma=1.54, degree=5)
        #model = svm.SVC(kernel='linear',decision_function_shape='ovr')#one vs rest
        #model = svm.SVC(kernel='linear',decision_function_shape='ovo')#one vs one
        model = svm.SVC(kernel='rbf', C=1, gamma=1)#radial basis function
        model.fit(classes, type_label)
        
        x_ts = t1
        y_ts = h1
        
        
        if(model.predict([[x_ts, y_ts]]))==0:
            print('belong to class = sunny!!')
            st = 'sunny'
        
        else:
            print('belong to class = cloudy or night!')
            st = 'cloudy or night'
        ##############################################
        msg = "DS16b20-Temperature= %s, HAT-Temperature= %s, Pressure= %s, Humidity= %s, Status= %s" %(t1,t2,p1,h1,st)
        sense.show_message(msg, scroll_speed=0.05,back_colour=bg)
        ######################
        url = "https://api.thingspeak.com/update?api_key=ZTUTDE6514D8SVK9"
        try :
            url = url+"&field1="+str(t1)
            url = url+"&field2="+str(t2)
            url = url+"&field3="+str(p1)
            url = url+"&field4="+str(h1)
            url = url+"&status="+str(st)
            resp = proxy.request('GET', url)
            content = resp.read()
            # You don't actually need to release_conn() if you're reading the full response.
            # This will be a harmless no-op:
            resp.release_conn()
            print (content)
            print ('Thingspeak updated!!!')
        except :
            print ("connection failed")
        ######################
        file_path = "/home/pi/Desktop/iot_west_pics/log/date_log.txt"
        with open(file_path, 'a') as file:
            time1 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            file.write( 'IoT lab-west:,'+'Date:'+str(time1)+"\n")
            file.write(msg+"\n")
        file.close()
        ######################
        msg1=""
        sense.show_message(msg1,back_colour=bg_exit)
        ##################
        time.sleep(900)
        #wait()
        ###################
except KeyboardInterrupt:
    msg1=""
    sense.show_message(msg1,back_colour=bg_exit)
    pass