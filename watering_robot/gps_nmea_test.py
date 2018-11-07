import serial
import pynmea2
ser = serial.Serial ("/dev/ttyS0")    #Open named port 
while 1:
    try:
        data = ser.readline()
        if data[0:6] == '$GPGGA':                     #Set baud rate t
            msg = pynmea2.parse(data)
            print(msg.lat)
            print(msg.lon)
        else:
            pass
    except:
        print("nothing is what it seem")
        pass