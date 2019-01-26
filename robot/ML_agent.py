#!/usr/bin/env python3
# import modules 
#from gps3 import gps3
#import serial
import math
import time
import csv
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
    in_lat = 10.724330
    in_lon = 99.374710
    k = 1

    with open('robot/lat_lon.csv', newline='') as f:
        read = csv.reader(f)
        for gps_row in read:
            print(gps_row) # check if gps read properly
            try:
                lat_b = float(gps_row[0]) #unpack list to float
                lon_b = float(gps_row[1])
            except IndexError as identifier:
                os.system('cls||clear')
                print('Indexing Error')
                #ser.write(str.encode('S'))
                print('Serial_STOP')
                break
            # main function
            while (distance > 5):            
                
                distance = h_sin(in_lat, in_lon, lat_b, lon_b)       
                os.system('cls||clear')
                print("Distance : ", "{0:.4} meter".format(distance), "\nStatus : Running")
                
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
                print("\nDistance offset: ", "{0:.4} meter".format(distance), " Status : Stop")
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

def h_sin(in_lat, in_lon, lat_b, lon_b):
    earth_radius = 6371e3
    lat_A = math.radians(in_lat)    #convert incoming latitude to rad
    lat_B = math.radians(lat_b)     #convert store latitude to rad
    del_lat = math.radians(lat_b-(in_lat))
    del_lon = math.radians(lon_b-(in_lon))
    a = (math.sin(del_lat/2)*math.sin(del_lat/2))+math.cos(del_lat*math.cos(lat_B))*(math.sin(del_lon/2)*math.sin(del_lon/2))

    try:
        c = 2*math.atan2(math.sqrt(a), math.sqrt((1-a)))
    except ValueError:
        print("No Value")
    return earth_radius*c
    
if __name__ == '__main__':
    
    try:
        main()
    except KeyboardInterrupt:
        print('Serial_STOP')
        #ser.write(str.encode('S'))
        raise Exception('Interrupt...Program terminated.')
        



