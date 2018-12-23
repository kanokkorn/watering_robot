import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600)
def main():
    for i in range(0, 100):
        ser.write(str.encode('B'))
        time.sleep(1)
    ser.write(str.encode('S'))
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        ser.write(str.encode('S'))
        print('Serial_STOP')
        raise Exception('Interrupt...Program terminated.')