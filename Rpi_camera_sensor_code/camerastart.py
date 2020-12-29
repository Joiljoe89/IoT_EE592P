import picamera
import time
camera = picamera.PiCamera()
camera.vflip=True
"""camera.capture('ex1.jpg')
"""
camera.start_recording('ex1vid.h264')
time.sleep(5)
camera.stop_recording
