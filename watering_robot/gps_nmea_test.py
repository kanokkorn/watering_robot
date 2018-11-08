import serial
import pynmea2
import time 
    #Open named port 
while 1:
    try:
        ser = serial.Serial ("/dev/ttyS0", 9600, timeout = 0.01)
        datastream = pynmea2.NMEAStreamReader()
        data = ser.readline()
        if data[0:6] == '$GPGGA':                     #Set baud rate t
            msg = pynmea2.parse(data)
            print(msg.lat, msg.lon)
            time.sleep(0.01)
    except:
        print("nothing is what it seem")
        time.sleep(0.01)
        pass