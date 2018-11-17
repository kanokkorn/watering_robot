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

'''with open('watering_robot/lat_lon_test.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
    read_csv = csv.reader(csvfile, delimiter=',')
    geo_list = list(read_csv)'''

for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        print('Altitude = ', data_stream.TPV['lat'], 'Latitude = ', data_stream.TPV['lon'])
        if (data_stream.TPV['lat'] == 'n/a') or (data_stream.TPV['lon'] != 'n/a'):
            pass

        if (data_stream.TPV['lat'] != '10.72543') or (data_stream.TPV['lon'] != '99.375431'):
            try:
                lat_A = math.radians(float(data_stream.TPV['lat']))
            except ValueError:
                print("GPS pass N/A value")
            try:
                lon_A = math.radians(float(data_stream.TPV['lon']))
            except ValueError:
                print("GPS pass N/A value")
            lat_B = math.radians(10.725416)
            lon_B = math.radians(99.375431)
            del_lat = (10.725416-float(data_stream.TPV['lat']))
            del_lon = (99.375431-float(data_stream.TPV['lon']))
            a = math.sin(del_lat/2)*math.sin(del_lat/2)+math.cos(lat_A)*math.cos(lat_B)*math.sin(del_lon)
            c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
            distance = earth_radius*c

            if (distance > 0.5):
                print("distance: ", distance)
                print("MOVE")
                ser.write(str.encode('M'))
            elif (distance < 0.5):
                print("distance: ", distance)
                print("STOP")
                ser.write(str.encode('S'))
                pass

        elif  (data_stream.TPV['lat'] == '10.72543') or (data_stream.TPV['lon'] == '99.375431'):
            print("STOP")
            ser.write(str.encode('S'))
            break