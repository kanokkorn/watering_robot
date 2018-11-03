import serial
import pynmea2

ser = serial.Serial ("/dev/ttyS0", 9600, timeout = 0.5)    #Open named port 
ser.open()
while 1:
    try:
        data = ser.readline()
        if data[0:6] == '$GPGGA':                     #Set baud rate t
            msg = pynmea2.parse(data)
            print(msg.lat)
            print(msg.lon)
    except:
        print("nothing is what it seem")
        pass