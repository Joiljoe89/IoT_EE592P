import picamera
import time
camera=picamera.PiCamera()
camera.vflip=True
camera.capture('ex1.jpg')
time.sleep(5)
camera.capture('ex2.jpg')

#terminal $ raspistill -o "image.jpg"