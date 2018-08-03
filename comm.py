import serial

ser = serial.Serial('COM3', 38400, timeout=0)
print(ser.name)
ser.write(b'initialize...')
ser.isOpen()

def serial(act_str):
    try:
        cmd = str(input(act_str))
        ser.write(cmd)
        print(cmd)
    except KeyboardInterrupt:
        raise       
if __name__ == '__main__':
    print("comm is connect directly")
else:
    print("comm is imported")

    