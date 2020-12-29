import time
import picamera
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
        with picamera.PiCamera() as camera:
            camera.resolution = (480, 360)
            camera.rotation = 0
            ####################
            time.sleep(900)
            #wait()
            #####################
            for filename in camera.capture_continuous('west_img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
                print('Captured %s' % filename)
                ############
                read_ser=ser.readline()
                t1= read_ser
                t1= t1[0:4]
                t1=float(t1)
                ########
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
                    
                msg = "ds16b20-Temperature= %s, HAT-Temperature= %s, Pressure= %s, Humidity= %s" %(t1,t2,p1,h1)
                sense.show_message(msg, scroll_speed=0.05,back_colour=bg)
                msg1=""
                sense.show_message(msg1,back_colour=bg_exit)
                #############
                url = "https://api.thingspeak.com/update?api_key=PHC31VGTSK2YSNT1"
                try :
                    url = url+"&field1="+str(t1)
                    url = url+"&field2="+str(t2)
                    url = url+"&field3="+str(p1)
                    url = url+"&field4="+str(h1)
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
                file_path = "/home/pi/Desktop/iot_west_pics/log/date_log.txt"
                with open(file_path, 'a') as file:
                    time1 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    file.write( 'IoT lab-West:,'+'Date:'+str(time1)+"\n")
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