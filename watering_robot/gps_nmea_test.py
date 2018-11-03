import serial
import pynmea2

import serial
ser = serial.Serial ("/dev/ttyS0")    #Open named port 
ser.baudrate = 9600                     #Set baud rate to 9600
data = ser.read(60)                     #Read ten characters from serial port to data
msg = pynmea2.parse(data)
print(msg.lat, msg.lat)                        #Send back the received data
ser.close() 