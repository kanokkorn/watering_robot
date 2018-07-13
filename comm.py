import serial

def comm(ser):
    ser = serial.Serial('COM3', 38400, timeout=0)
    print(ser.name)
    ser.write(b'initialize...')
    ser.isOpen()
if __name__ == '__main__':
    print("comm is connect directly")
else:
    print("comm is imported")

    