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
#from gps3 import gps3
#import serial
import math
import time
import csv
import torch
#import classify_edit
import sys
import os
# setup gps socket
'''#ser = serial.Serial('/dev/ttyUSB0', 9600)
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
'''

#read csv files
def main():
    # prefix parameter for test
    distance = 10
    earth_radius = 6371e3

    in_lat = 10.725450
    in_lon = 99.375350
    k = 1
    with open('watering_robot/lat_lon.csv', newline='') as f:
        read = csv.reader(f)
        for gps_row in read:
            #print(gps_row) # check if gps read properly
            lat_b = float(gps_row[0]) #unpack list to float
            lon_b = float(gps_row[1]) 
            # main function
            while (distance > 6):            
                lat_A = math.radians(in_lat)
                lat_B = math.radians(lat_b)
                del_lat = math.radians(lat_b-(in_lat))
                del_lon = math.radians(lon_b-(in_lon))
                a = (math.sin(del_lat/2)*math.sin(del_lat/2))+math.cos(lat_A)*math.cos(lat_B)*(math.sin(del_lon/2)*math.sin(del_lon/2))
                # check if equal zero
                try:
                    c = 2*math.atan2(math.sqrt(a), math.sqrt((1-a)))
                except ValueError:
                    print("No Value")
                distance = earth_radius*c        
                os.system('cls||clear')
                print("Distance: ", distance, "\nStatus : Running")
                
                #print("Serial_MOVE")
                in_lat += 0.0000005
                in_lon += 0.0000005
                time.sleep(0.08)
                #ser.write(str.encode('M'))

            else:
                #ser.write(str.encode('S'))
                os.system('cls||clear')
                print('==== Checkpoint ', k," start ====")
                time.sleep(0.3)
                print("\nDistance: ", distance, " Status : Stop")
                time.sleep(0.3)
                #print("Serial_STOP")
                time.sleep(0.3)
                print("\nClassification palm Tree :"+ str(k)+"\n")
                #classify_edit.main()
                time.sleep(0.3)
                for target in range(10):
                    print("writing csv files"+"."*target, end="\r")
                    time.sleep(0.5)
                print('\n')
                distance = 10
                in_lat = lat_b
                in_lon = lon_b
                print("==== Checkpoint", k, " done ====\n")
                k += 1
                time.sleep(0.5)
                print("Start Moving to next checkpoint\n")
                time.sleep(1)
        else:
            os.system('cls||clear')
            print('==== End of lines ====')
            time.sleep(0.5)
            print('\nFinished\n')

if __name__ == '__main__':
    
    try:
        main()
    except KeyboardInterrupt:
        print('Serial_STOP')
        #ser.write(str.encode('S'))
        raise Exception('Interrupt...Program terminated.')
        



