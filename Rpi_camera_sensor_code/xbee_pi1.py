"""
by joe
This example continuously reads the serial port and processes IO data
received from a remote XBee.
"""

from xbee import ZigBee
import serial
import struct
import time
def hex(bindata):
    return ''.join('%02x' % ord(byte) for byte in bindata)

PORT = '/dev/ttyUSB3'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = ZigBee(ser,escaped=True)

# Continuously read and print packets
while True:
    try:
        response = xbee.wait_read_frame()
        print response
        sa=hex(response['source_addr_long'][4:])
        #rf=hex(response['rf_data'][0:5])
        #datalength=len(rf)
        
        print(time.strftime('%x %X %Z'),' ',response['source_addr_long'][4:7]+response['source_addr_long'][7:],"temp:",response['rf_data'][0:2],",","humidity:",response['rf_data'][4:6])
    
        
    except KeyboardInterrupt:
        break

ser.close()