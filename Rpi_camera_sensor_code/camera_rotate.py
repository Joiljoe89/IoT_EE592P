from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(10)
camera.stop_preview()
######
camera.rotation = 90
camera.start_preview()
sleep(10)
camera.stop_preview()