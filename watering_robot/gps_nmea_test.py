import serial
import pynmea2
import time

ser = serial.Serial ("/dev/ttyS0")    #Open named port
streamread = pynmea2.NMEAStreamReader()

while 1:
    
    try:
        data = ser.readline()
        for msg in streamreader.next(data):
            print(msg.lat)
            print(msg.lon)
        '''if data[0:6] == '$GPGGA':                     #Set baud rate t
            msg = pynmea2.parse(data)
            print(msg.lat)
            print(msg.lon)
            time(0.005)'''
        if data[0:6] == '$GPRMC':
            print("Not what we want")
            time(0.005)
        elif data[0:6] == '$GPVTG':
            print("Not that too")
            time(0.005)
    except:
        print("nothing is what it seem")
        time(0.005)