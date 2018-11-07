import serial
import pynmea2
import time 
ser = serial.Serial ("/dev/ttyS0")    #Open named port 
while 1:
    try:
        data = ser.readline()
        if data[0:6] == '$GPGGA':                     #Set baud rate t
            msg = pynmea2.parse(data)
            print(msg.lat)
            print(msg.lon)
            time.sleep(0.01)
        else:
            pass
    except:
        print("nothing is what it seem")
        time.sleep(0.01)
        pass