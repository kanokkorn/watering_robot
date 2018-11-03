import serial
import pynmea2

import serial
ser = serial.Serial ("/dev/ttyS0")    #Open named port 
ser.baudrate = 9600
data = ser.read(60)
if data[0:6] == '$GPGGA':                     #Set baud rate t
    msg = pynmea2.parse(data)
    print(msg.lat, msg.lat)                        #Send back the received data
ser.close() 