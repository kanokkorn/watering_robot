import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600)
def main():
    sig_in = str.encode(input(str("Press: ")))
    while (sig_in != 0):
        ser.write(sig_in)
    else:
        ser.write(str.encode('S'))
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        ser.write(str.encode('S'))
        print('Serial_STOP')
        raise Exception('Interrupt...Program terminated.')