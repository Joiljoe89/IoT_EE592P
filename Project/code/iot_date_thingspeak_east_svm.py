import time
import picamera
import pandas as pd
#lib for analysis
import numpy as np
from sklearn import svm
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
            time.sleep(100)
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
                
                
                if(model.predict([[x_ts, y_ts]]))==0:
                    print('belong to class = sunny!!')
                    st = 'sunny'
                        
                elif(model.predict([[x_ts, y_ts]]))==1:
                    print('belong to class = cloudy!!')
                    st = 'cloudy'
                        
                else:
                    print('belong to class = night!')
                    st = 'night'
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
                file_path = "/home/pi/Desktop/iot project/east data/log/date_log.txt"
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
