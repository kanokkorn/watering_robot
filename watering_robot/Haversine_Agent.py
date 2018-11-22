'''
Copyright (c) [2018] [Kanokkorn]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
# import modules 
from gps3 import gps3
import serial
import math
import time
import csv

# setup gps socket
ser = serial.Serial('/dev/ttyUSB0', 9600)
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()


# prefix parameter for 
distance = 100
earth_radius = 6371e3

#read csv files
with open('./watering_robot/lat_lon.csv', 'rtU', newline='') as f:
    read = csv.reader(f)
    for gps_row in read:
        print(gps_row)
        lat_b = float(gps_row[0]) #unpack list to float
        lon_b = float(gps_row[1]) 
        
        # main function
        while (distance >= 3):
            for new_data in gps_socket:
                if new_data:
                    data_stream.unpack(new_data)
                    print('Altitude = ', data_stream.TPV['lat'], 'Latitude = ', data_stream.TPV['lon'])
                    if (data_stream.TPV['lat'] == 'n/a') or (data_stream.TPV['lon'] != 'n/a'):
                        pass
                    if (data_stream.TPV['lat'] != '10.0') or (data_stream.TPV['lon'] != '10.0'):
                        try:
                            in_lat = float(data_stream.TPV['lat'])
                        except ValueError:
                            print("lat N/A value")
                            in_lat = (10.712709)
                        try:
                            in_lon = float(data_stream.TPV['lon'])
                        except ValueError:
                            print("lon N/A value")
                            in_lon = (99.378788)
                    lat_A = math.radians(in_lat)
                    lat_B = math.radians(lat_b)
                    del_lat = math.radians(lat_b-(in_lat))
                    del_lon = math.radians(lon_b-(in_lon))
                    a = (math.sin(del_lat/2)*math.sin(del_lat/2))+math.cos(lat_A)*math.cos(lat_B)*(math.sin(del_lon/2)*math.sin(del_lon/2))
                
                    # check if equal zero
                    try:
                        c = 2*math.atan2(math.sqrt(a), math.sqrt((1-a)))
                    except ValueError as identifier:
                        print("No Value")
                    distance = earth_radius*c        
                    print("distance: ", distance)
                    print("MOVE")
                    ser.write(str.encode('M'))

            else :
                print("distance: ", distance)
                print("STOP")
                ser.write(str.encode('S'))
                for xtime in range(20):
                    ser.write(str.encode('BLNK_ON'))
                    time.sleep(.2)
                    ser.write(str.encode('BLNK_OF'))
                    time.sleep(.2)
                pass

