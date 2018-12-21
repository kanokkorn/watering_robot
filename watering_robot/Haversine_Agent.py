# 
# Copyright (c) 2019 Kanokkorn
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================

# import modules 

from gps3 import gps3
import serial
import math
import time
import csv
import os
# setup gps socket
ser = serial.Serial('/dev/ttyUSB0', 9600)
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()


#read csv files
def track():
    
    # prefix parameter
    distance = 10
    earth_radius = 6371e3

    in_lat = 10.725450
    in_lon = 99.375350
    k = 1
    with open('watering_robot/lat_lon.csv', newline='') as f:
        read = csv.reader(f)
        for gps_row in read:
            #print(gps_row) # check if gps read properly
            try:
                lat_b = float(gps_row[0]) #unpack list to float
                lon_b = float(gps_row[1])
            except IndexError:
                ser.write(str.encode('S'))
                raise Exception('Indexing error...Program termonated')

            # main function
            for new_data in gps_socket:
                if (new_data and distance > 5):
                    data_stream.unpack(new_data)
                    #print('Altitude = ', data_stream.TPV['lat'], 'Latitude = ', data_stream.TPV['lon'])
                    
                    if (data_stream.TPV['lat'] == 'n/a') or (data_stream.TPV['lon'] != 'n/a'):
                        pass
                    if (data_stream.TPV['lat'] != 'n/a') or (data_stream.TPV['lon'] != 'n/a'):
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
                    os.system('cls||clear')
                    print("Distance: ", distance, " Status : Running")
                    ser.write(str.encode('M'))
                    
                elif (new_data and distance < 5 ):

                    ser.write(str.encode('S'))
                    os.system('cls||clear')
                    print('\n==== Checkpoint ', k," start ====")
                    time.sleep(0.3)
                    print("\nDistance: ", distance, " Status : Stop")
                    time.sleep(0.3)
                    print("Serial_STOP")
                    time.sleep(0.3)
                    for target in range(10):
                        ser.write(str.encode('O'))
                        print("watering"+"."*target, end="\r")
                        ser.write(str.encode('P'))
                        time.sleep(0.8)
                    time.sleep(0.3)
                    print("\nClassification palm Tree :"+ str(k))
                    time.sleep(0.3)
                    #classify_edit.main()
                    for target in range(10):
                        print("writing csv files"+"."*target, end="\r")
                        time.sleep(0.8)
                    distance = 10
                    in_lat = lat_b
                    in_lon = lon_b
                    print("\n==== Checkpoint", k, " done ====\n")
                    k += 1
                    time.sleep(1)
                    print("Start Moving to next checkpoint\n")
                    time.sleep(1)
        else:
            ser.write(str.encode('S'))
            os.system('cls||clear')
            print('\n==== End of lines ====')
            time.sleep(1)
            print('\nFinished\n')

if __name__ == '__main__':
    try:
        track()
    except KeyboardInterrupt:
        print('Serial_STOP')
        ser.write(str.encode('S'))
        raise Exception('Interrupt...Program terminated.')
        