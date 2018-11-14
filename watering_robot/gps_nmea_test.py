from gps3 import gps3
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        print('Altitude = ', data_stream.TPV['lat'], 'Latitude = ', data_stream.TPV['lon'])
        if (data_stream.TPV['lat'] != '10.725359') or (data_stream.TPV['lon'] != '99.375334'):
            print("MOVE")
            ser.write(str.encode('M'))
        elif  (data_stream.TPV['lat'] == '10.725359') or (data_stream.TPV['lon'] == '99.375334'):
            print("STOP")
            ser.write(str.encode('S'))
            break