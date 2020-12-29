"""
by joe d17024
this is an example continuously reads the serial port and processes IO data received from a remote Xbee
"""

from xbee import Zigbee
import serial
import struct
import time
def hex(bindata):
    return ''.join('%02x' %ord(byte) for byte in bindata)

PORT = 'dev/ttyUSB3' #ls -l /dev/tty*
BAUD_RATE = 9600

#open serial port
ser = serial.Serial(PORT,BAUD_RATE)

#create API object
xbee = ZigBee(ser,escaped=True)

#continously read and print packets
while True:
    try:
        response = xbee.wait_read_frame()
        print response
        sa = hex(reponse['source_addr_long'][4:])

        print(time.strftime('%x %X %Z'),' ',response['source_addr_long'][4:7]+response['source_addr_long'][7:],"temp:",response['rf_data'][0:2],",","humidity:",response["rf_data"][4:6])

    except KeyboardTnterrupt:
        break

ser.close()
