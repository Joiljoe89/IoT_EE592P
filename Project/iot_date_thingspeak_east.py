import time
import picamera
from datetime import datetime, timedelta
from time import gmtime, strftime
from sense_hat import SenseHat
sense = SenseHat()
bg_exit=[0,0,0]
###
import urllib3
proxy = urllib3.ProxyManager('https://10.8.0.1:8080/')

try:
    while True:
        '''
        def wait():
            # Calculate the delay to the start of the next hour
            next_hour = (datetime.now() + timedelta(hour=1)).replace(
                minute=0, second=0, microsecond=0)
            delay = (next_hour - datetime.now()).seconds
            time.sleep(delay)
        '''
        with picamera.PiCamera() as camera:
            camera.resolution = (480, 360)
            camera.rotation = 90
            ####################
            time.sleep(900)
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
                #############
                url = "https://api.thingspeak.com/update?api_key=0CUYIC4MJ5PMGQQF"
                try :
                    url = url+"&field1="+str(t1)
                    url = url+"&field2="+str(p1)
                    url = url+"&field3="+str(h1)
                    #url = url+"&field4="+str(data['HUM'])
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
                time.sleep(900)
                #wait()
                ###################
except KeyboardInterrupt:
    
    msg1=""
    sense.show_message(msg1,back_colour=bg_exit)
    pass
