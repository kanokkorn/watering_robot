from gps3 import gps3
import serial
import math

ser = serial.Serial('/dev/ttyUSB0', 9600)
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
earth_radius = 6371e3
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
                in_lat = float(data_stream.TPV['lat'])
            except ValueError:
                print("lat N/A value")
                lat_A = (10.712676)
            try:
                in_lon = float(data_stream.TPV['lon'])
            except ValueError:
                print("lon N/A value")
                lon_A = (99.375075)
            lat_A = math.radians(in_lat)
            lat_B = math.radians(10.712767)
            del_lat = math.radians(10.712767-(in_lat+0.005))
            del_lon = math.radians(99.378638-(in_lat+0.005))
            a = (math.sin(del_lat/2)*math.sin(del_lat/2))+math.cos(lat_A)*math.cos(lat_B)*(math.sin(del_lon/2)*math.sin(del_lon/2))
            try:
                c = 2*math.atan2(math.sqrt(a), math.sqrt((1-a)))
            except ValueError as identifier:
                print("No Value")
            distance = earth_radius*c

            if (distance > 1):
                print("distance: ", distance)
                print("MOVE")
                ser.write(str.encode('M'))
            elif (distance < 1):
                print("distance: ", distance)
                print("STOP")
                ser.write(str.encode('S'))
                pass