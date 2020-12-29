import RPi.GPIO as GPIO
import time

import datetime

c=0
for c in range(1,100,1):
    from time import gmtime, strftime
    t = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    import Adafruit_DHT
    sensor=Adafruit_DHT.DHT11
    gpio=27
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temperature is not None:
        th=('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
      print('Failed to get reading. Try again!')

    #file = open("/home/pi/Desktop/iot4.txt", "w")
    file_path = "/home/pi/Desktop/iot4.txt"
    with open(file_path, 'a') as file:
        file.write( 'IoT Lab:,'+'Date:'+str(t)+"\n")
        file.write('temperature'+str(th[5:7])+',humidity'+str(th[22:24])+"\n")

    file.close()
    c=c+1
    time.sleep(1800)
print(c)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#power sensor
GPIO.setup(4,GPIO.OUT)
time.sleep(1)
print "Sensor 'on'"
GPIO.output(4,GPIO.HIGH)
#led 
GPIO.setup(26,GPIO.OUT)
print "Green LED 'on'"
GPIO.output(26,GPIO.HIGH)

#US distance in CM
trig=23
echo=24

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

GPIO.output(trig,False)
time.sleep(1)

GPIO.output(trig,True)
time.sleep(0.00001)
GPIO.output(trig,False)

while GPIO.input(echo)==0:
    pulse_start=time.time()
    
while GPIO.input(echo)==1:
    pulse_end=time.time()

pulse_duration = pulse_end - pulse_start

distance=pulse_duration*2000
distance=round(distance,2)

print "Distance:",distance,"cm"

print "Green LED 'off'"
GPIO.output(4,GPIO.LOW)
GPIO.output(26,GPIO.LOW)
print "Sensor 'off'"
GPIO.cleanup()
