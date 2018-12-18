import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
def main():
    while 1:
        ser.write(str.encode('B'))
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Serial_STOP')
        ser.write(str.encode('S'))
        raise Exception('Interrupt...Program terminated.')