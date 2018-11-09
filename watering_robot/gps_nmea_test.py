import serial
import pynmea2
import time 

while 1:
    print("Start testing ...")
    ser = serial.Serial ("/dev/ttyS0", 9600, timeout = 1)
    datastream = pynmea2.NMEAStreamReader()
    data = ser.readline()
    if data[0:6] == '$GPGGA':                    
        msg = pynmea2.parse(data)
        print(msg.lat, msg.lon)
        time.sleep(1)
    elif data[0:6] == '$GPTXT':                    
        print("that's not it")
        time.sleep(1)