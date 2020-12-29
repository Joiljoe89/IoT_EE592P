import time
import picamera
from datetime import datetime, timedelta
from time import gmtime, strftime
import serial
from sense_hat import SenseHat
sense = SenseHat()

bg_exit=[0,0,0]

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
        ser=serial.Serial("/dev/ttyACM0",9600)
        ser.baudrate=9600
        with picamera.PiCamera() as camera:
            camera.resolution = (480, 360)
            camera.rotation = 0
                        
            time.sleep(900)
            #wait()
            #####################
            for filename in camera.capture_continuous('north_img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
                print('Captured %s' % filename)
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
                    
                msg = "DS16b20-Temperature= %s, HAT-Temperature= %s, Pressure= %s, Humidity= %s" %(t1,t2,p1,h1)
                sense.show_message(msg, scroll_speed=0.05,back_colour=bg)
                    
                file_path = "/home/pi/Desktop/iot project/date/log/date_log.txt"
                with open(file_path, 'a') as file:
                    time1 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    file.write( 'IoT lab-North:,'+'Date:'+str(time1)+"\n")
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