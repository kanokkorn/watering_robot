import serial

def comm(args):
    ser = serial.Serial('COM3', 38400, timeout=0)  # open serial port
    print(ser.name)         # check which port was really used
    ser.write(b'hello')
    
if __name__ == '__main__':
    print("comm is connect directly")
else:
    print("comm is imported")

    