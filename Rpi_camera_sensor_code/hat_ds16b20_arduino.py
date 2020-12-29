import serial
from sense_hat import SenseHat
sense = SenseHat()

try:
    while True:
        ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
        ser.baudrate=9600
    
        read_ser=ser.readline()
        #print(read_ser)
        #t= sense.get_temperature()
        t= read_ser
        p= sense.get_pressure()
    
        h= sense.get_humidity()
    
        t= t[0:4]
        t=float(t)
        #print(t)
    
        p1= round(p,1)
        #print(p1)
    
        h1= round(h,1)
        
        if t>=20.0 and t<35.0:
            bg=[0,100,0]
        else:
            if t<20.0:
                bg=[0,0,100]
            else:
                bg=[100,0,0]
        
        
        msg = "Temperature= %s, Pressure= %s, Humidity= %s" %(t,p1,h1)
    
        sense.show_message(msg, scroll_speed=0.05,back_colour=bg)
except KeyboardInterrupt:
    bg_exit=[0,0,0]
    msg1=""
    sense.show_message(msg1,back_colour=bg_exit)
    pass