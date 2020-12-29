import time
import picamera
from datetime import datetime, timedelta

from sense_hat import SenseHat
sense = SenseHat()
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
            ####################
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
                
            file_path = "/home/pi/Desktop/iot project/date/log/date_log.txt"
            with open(file_path, 'a') as file:
                file.write( 'IoT lab-West:,'+'Date:'+str(t)+"\n")
                file.write(msg+"\n")
            file.close()
            ######################
            time.sleep(300)
            #wait()
            #####################
            for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
                print('Captured %s' % filename)
                time.sleep(300)
                #wait()
                ###################
except KeyboardInterrupt:
    bg_exit=[0,0,0]
    msg1=""
    sense.show_message(msg1,back_colour=bg_exit)
    pass