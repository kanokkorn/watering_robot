import serial
ser = serial.Serial('COM3', 38400, timeout=0)  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()