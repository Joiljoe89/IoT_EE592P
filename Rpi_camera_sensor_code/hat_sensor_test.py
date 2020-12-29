from sense_hat import SenseHat
sense = SenseHat()

try:
    while True:
    
        t= sense.get_temperature()
    
        p= sense.get_pressure()
    
        h= sense.get_humidity()
    
        t1= round(t,1)
    
        p1= round(p,1)
    
        h1= round(h,1)
    
        if t1>20.0 and t1<35.0:
            bg=[0,100,0]
        else:
            bg=[100,0,0]
        
    
        msg = "Temperature= %s, Pressure= %s, Humidity= %s" %(t1,p1,h1)
    
        sense.show_message(msg, scroll_speed=0.05, back_colour=bg)
except KeyboardInterrupt:
    bg_exit=[0,0,0]
    msg1=""
    sense.show_message(msg1,back_colour=bg_exit)
    pass