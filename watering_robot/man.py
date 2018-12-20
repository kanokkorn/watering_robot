import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
def main():
        if str(input()) != None:
            ser.write(str.encode(str(input())))
            print(ser.write(str.encode(str(input()))))
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Serial_STOP')
        ser.write(str.encode('S'))
        raise Exception('Interrupt...Program terminated.')