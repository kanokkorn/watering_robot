from gps3 import gps3
import serial
import math

ser = serial.Serial('/dev/ttyUSB0', 9600)
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
earth_radius = 6371e3
x = 0

with open('watering_robot/lat_lon_test.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
    read_csv = csv.reader(csvfile, delimiter=',')
    geo_list = list(read_csv)

for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        print('Altitude = ', data_stream.TPV['lat'], 'Latitude = ', data_stream.TPV['lon'])
        if (data_stream.TPV['lat'] != '10.72543') or (data_stream.TPV['lon'] != '99.375431'):
            del_lat = math.log(math.tan(((math.pi)/4)+(((float(data_stream.TPV['lat']))/2))/math.tan(((math.pi)/4+((10.72543))/2))))
            del_lon = math.log(math.tan(((math.pi)/4)+(((float(data_stream.TPV['lon']))/2))/math.tan(((math.pi)/4+((99.375431))/2))))
            del_Q = (del_lat/del_lon)
            distance = math.sqrt(((del_lat)**2)+(del_Q**2)*earth_radius)

            if (distance > .5)
                print("MOVE")
                ser.write(str.encode('M'))
            elif (distance < .5):
                print("STOP")
                ser.write(str.encode('S'))
                pass

        elif  (data_stream.TPV['lat'] == '10.72543') or (data_stream.TPV['lon'] == '99.375431'):
            print("STOP")
            ser.write(str.encode('S'))
            break