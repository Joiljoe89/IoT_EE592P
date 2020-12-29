import time
import datetime

import serial
from sense_hat import SenseHat
sense = SenseHat()

try:
    while True:
        from time import gmtime, strftime
        t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        
        ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
        ser.baudrate=9600
    
        read_ser=ser.readline()
        #print(read_ser)
        #t= sense.get_temperature()
        t1= read_ser
        p= sense.get_pressure()
    
        h= sense.get_humidity()
    
        t1= t1[0:4]
        t1=float(t1)
        #print(t)
    
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
        
        file_path = "/home/pi/Desktop/iot4.txt"
        with open(file_path, 'a') as file:
            file.write( 'IoT lab-West:,'+'Date:'+str(t)+"\n")
            file.write(msg+"\n")
        file.close()
        time.sleep(300)
        
except KeyboardInterrupt:
    bg_exit=[0,0,0]
    msg1=""
    sense.show_message(msg1,back_colour=bg_exit)
    pass
