'''
MIT License

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

from gps3 import gps3
import serial
import math
import sys

ser = serial.Serial('/dev/ttyUSB0', 9600)
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
earth_radius = 6371e3

for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        print("====================================")
        sys.stdout.write('\r Altitude = %s' %data_stream.TPV['lat'], 'Latitude = %s' %data_stream.TPV['lon'])
        if (data_stream.TPV['lat'] == 'n/a') or (data_stream.TPV['lon'] != 'n/a'):
            pass
        if (data_stream.TPV['lat'] != '10.72543') or (data_stream.TPV['lon'] != '99.375431'):
            try:
                in_lat = float(data_stream.TPV['lat'])
            except ValueError:
                print("\r lat N/A value \n")
                in_lat = (10.712709)
            try:
                in_lon = float(data_stream.TPV['lon'])
            except ValueError:
                print("\r lon N/A value \n")
                in_lon = (99.378788)
            lat_A = math.radians(in_lat)
            lat_B = math.radians(10.725378)
            del_lat = math.radians(10.725378-(in_lat))
            del_lon = math.radians(99.375355-(in_lon))
            a = (math.sin(del_lat/2)*math.sin(del_lat/2))+math.cos(lat_A)*math.cos(lat_B)*(math.sin(del_lon/2)*math.sin(del_lon/2))
            try:
                c = 2*math.atan2(math.sqrt(a), math.sqrt((1-a)))
            except ValueError as identifier:
                print("\rNo Value")
            distance = earth_radius*c
            if (distance > 3):
                sys.stdout.write("\r distance: %f \n" %distance)
                sys.stdout.write("\r MOVE")
                ser.write(str.encode('M'))
                sys.stdout.write("\r ==================================== \n")
                sys.stdout.flush()
            elif (distance < 3 and distance != 0):
                sys.stdout.write("\r distance: %f \n" %distance)
                sys.stdout.write("\r STOP")
                ser.write(str.encode('S'))
                sys.stdout.write("\r ==================================== \n")
                sys.stdout.flush()
                break
            elif (distance == 0):
                sys.stdout.write("\r No value")
                sys.stdout.write("\r ==================================== \n")
                sys.stdout.flush()