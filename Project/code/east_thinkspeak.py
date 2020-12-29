# -*- coding: utf-8 -*-
"""
Created on Mon May 21 18:06:24 2018

@author: joe d17024
"""
import sys
import time
import picamera
#import httplib, urllib
import urllib2
from datetime import datetime, timedelta
from time import gmtime, strftime
from sense_hat import SenseHat
sense = SenseHat()
bg_exit=[0,0,0]
# Enter Your API key here
myAPI = 'ZTUTDE6514D8SVK9' 
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

try:
    while True:
        with picamera.PiCamera() as camera:
            camera.resolution = (480, 360)
            camera.rotation = 90
            ####################
            time.sleep(9)
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
                    
                msg = "Temperature= %s, Pressure= %s, Humidity= %s" %(t1,p1,h1)
                sense.show_message(msg, scroll_speed=0.05,back_colour=bg)
                ##########
                msg1=""
                sense.show_message(msg1,back_colour=bg_exit)
                ###############################################################
                '''
                params = urllib.urlencode({'field1': temp, 'key':'ZTUTDE6514D8SVK9' })
                headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}                
                conn = httplib.HTTPConnection("api.thingspeak.com:80")
                '''
                # Sending the data to thingspeak
                conn = urllib2.urlopen(baseURL + '&field1=%s&field3=%s' % (t1, p1))
                print(conn.read())
                # Closing the connection
                conn.close()
                '''
                try:                
                    conn.request("POST", "/update", params, headers)                    
                    response = conn.getresponse()                    
                    print temp                    
                    print response.status, response.reason                    
                    data = response.read()                    
                    conn.close()                
                except:                
                    print "connection failed"
                '''
                #############
                file_path = "/home/pi/Desktop/iot project/east data/log/date_log.txt"
                with open(file_path, 'a') as file:
                    time1 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    file.write( 'IoT lab-East:,'+'Date:'+str(time1)+"\n")
                    file.write(msg+"\n")
                file.close()
                ######################
                time.sleep(9)
                #wait()
                ###################
except KeyboardInterrupt:
    
    msg1=""
    sense.show_message(msg1,back_colour=bg_exit)
    pass

