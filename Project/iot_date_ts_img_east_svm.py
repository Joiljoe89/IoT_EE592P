import time
import picamera
import pandas as pd
#lib for analysis
import numpy as np
import cv2
from sklearn import svm
from sklearn.decomposition import PCA

from time import gmtime, strftime
from sense_hat import SenseHat
sense = SenseHat()
bg_exit=[0,0,0]
###
import urllib3
proxy = urllib3.ProxyManager('https://10.8.0.1:8080/')

try:
    while True:
        
        with picamera.PiCamera() as camera:
            camera.resolution = (480, 360)
            camera.rotation = 90
            ####################
            time.sleep(10)
            #wait()
            #####################
            for filename in camera.capture_continuous('east_img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
                print('Captured %s' % filename)
                ##########
                t= sense.get_temperature()
                p= sense.get_pressure()
                h= sense.get_humidity()
                
                t1= round(t,1)
                
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
                blue = cv2.imread('/home/pi/Desktop/iot_project/project_data/iot_data/code'+'east_img{timestamp:%Y-%m-%d-%H-%M}.jpg')
                # calculate the histogram
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
    
                fv_pca = [0]
                fv1 = []
                histb = np.histogram(blue,bins=256)
                hb=histb[0]
                fvb1 = [[0,0,0,0,0,0,0,0]]
                for i in range(0,(hb.shape[0]),8):
                    fvb = hb[i:i+8]
                
                    pca = PCA(n_components=1)
                    pca.fit(fvb)
                    X_pca = pca.transform(fvb)
                    print("transformed shape:", X_pca.shape)
                    fv_pca = np.concatenate((fv_pca,X_pca),axis=0)
                    fv1[i]=X_pca[i]
                #############################################################
                #read training data
                tr_all = pd.read_csv('/home/pi/Desktop/iot_project/project_data/iot_data/west/west_hist_img_8bin_pca.csv',delimiter=',')
                
                '''
                x1 = X_pca[0]
                x2 = X_pca[1]
                x3 = X_pca[2]
                x4 = X_pca[3]
                x5 = X_pca[4]
                x6 = X_pca[5]
                x7 = X_pca[6]
                x8 = X_pca[7]
                x9 = X_pca[8]
                x10 = X_pca[9]
                x11 = X_pca[10]
                x12 = X_pca[11]
                x13 = X_pca[12]
                x14 = X_pca[13]
                x15 = X_pca[14]
                x16 = X_pca[15]
                x17 = X_pca[16]
                x18 = X_pca[17]
                x19 = X_pca[18]
                x20 = X_pca[19]
                x21 = X_pca[20]
                x22 = X_pca[21]
                x23 = X_pca[22]
                x24 = X_pca[23]
                x25 = X_pca[24]
                x26 = X_pca[25]
                x27 = X_pca[26]
                x28 = X_pca[27]
                x29 = X_pca[28]
                x30 = X_pca[29]
                x31 = X_pca[30]
                x32 = X_pca[31]
                x33 = X_pca[32]
                '''
                ####################################
                #read training data
                tr_all_class = pd.read_csv('/home/pi/Desktop/iot_project/project_data/iot_data/west/west_temp_humd.csv',delimiter=',')
                
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
                
                x_ts = t1
                y_ts = h1
                
                
                if(model.predict([[x_ts, y_ts]]))==1:
                    print('belong to class = cloudy!!')
                    st = 'cloudy'
                   
                else:
                    print('belong to class = sunny!')
                    st = 'sunny'
                ####################################
                msg = "Temperature= %s, Pressure= %s, Humidity= %s, status= %s" %(t1,p1,h1,st)
                sense.show_message(msg, scroll_speed=0.05,back_colour=bg)
                ##########
                msg1=""
                sense.show_message(msg1,back_colour=bg_exit)
                #############
                url = "https://api.thingspeak.com/update?api_key=0CUYIC4MJ5PMGQQF"
                try :
                    url = url+"&field1="+str(t1)
                    url = url+"&field2="+str(p1)
                    url = url+"&field3="+str(h1)
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
                #############
                file_path = "/home/pi/Desktop/iot_project/east_data/log/date_log.txt"
                with open(file_path, 'a') as file:
                    time1 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    file.write( 'IoT lab-East:,'+'Date:'+str(time1)+"\n")
                    file.write(msg+"\n")
                file.close()
                ######################
                time.sleep(100)
                #wait()
                ###################
except KeyboardInterrupt:
    
    msg1=""
    sense.show_message(msg1,back_colour=bg_exit)
    pass
