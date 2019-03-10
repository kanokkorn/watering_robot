#!/usr/bin/env python3

from gps3 import gps3
import serial
import math
import time
import csv
import sys
import os
# setup gps socket
ser = serial.Serial('/dev/ttyUSB0', 9600)
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()


#read csv files
def main():
    
    # assign parameter for testing
    distance = 10
    earth_radius = 6371e3
    in_lat = 10.712806
    in_lon = 99.378673
    count = 1

    with open('robot/lat_lon.csv', newline='') as f:
        read = csv.reader(f)
        for gps_row in read:
            
            # check if gps read properly
            print(gps_row)
            try:
                lat_b = float(gps_row[0]) #unpack list to float
                lon_b = float(gps_row[1])
            except IndexError as identifier:
                os.system('clear')
                print('Indexing Error')
                #ser.write(str.encode('S'))
                print('Serial_STOP')
                break
            
            # If robot distance is more than offset. keep running 
            for new_data in gps_socket:
                while (new_data and distance > 5):
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
                    distance = h_sin(in_lat, in_lon, lat_b, lon_b)  
                    angle = angl(in_lat, in_lon, lat_b, lon_b)     
                    os.system('clear')
                    print("Distance : ", "{0:.6} meter".format(distance),"\nAngle : ","{0:.6} Degree".format(angle),"\nHeading : N/A", "\nStatus : Running")
             
                # If robot distance is less than offset. Stop running and do the task
                else:
                    task(distance,count,in_lat, in_lon, lat_b, lon_b)
        else:
            os.system('clear')
            print('==== End of lines ====')
            time.sleep(0.5)
            print('\nFinished\n')
            exit()

# calculate distance between 2 points
def h_sin(in_lat, in_lon, lat_b, lon_b):
    earth_radius = 6371e3
    lat_A = math.radians(in_lat)    #convert incoming latitude to rad
    lat_B = math.radians(lat_b)     #convert store latitude to rad
    del_lat = math.radians(lat_b-(in_lat))
    del_lon = math.radians(lon_b-(in_lon))
    a = (math.sin(del_lat/2)*math.sin(del_lat/2))+math.cos(del_lat*math.cos(lat_B))*(math.sin(del_lon/2)*math.sin(del_lon/2))

    #catch erorr if < 0 
    try: 
        c = 2*math.atan2(math.sqrt(a), math.sqrt((1-a)))
    except ValueError:
        print("No Value")
    return earth_radius*c

# calculate angle between 2 points
def angl(in_lat, in_lon, lat_b, lon_b):
    y = math.sin(lon_b-in_lon) * math.cos(lat_b)
    x = math.cos(in_lat)*math.sin(lat_b)-math.sin(in_lat)*math.cos(lat_b)*math.cos(lon_b-in_lon)
    brng = math.degrees(math.atan2(y, x))
    return brng

def task(distance,count,in_lat, in_lon, lat_b, lon_b):
    os.system('clear')
    print('==== Checkpoint ', count," start ====")
    time.sleep(0.2)
    print("\nDistance offset: ", "{0:.4} meter".format(distance),"Status : Stop")
    time.sleep(0.2)
    #print("Serial_STOP")
    time.sleep(0.2)
    print("\nClassification palm Tree :"+ str(count)+"\n")
    #classify_edit.main()
    time.sleep(0.2)
    for target in range(10):
        print("writing csv files"+"."*target, end="\r")
        time.sleep(0.2)
    print('\n')
    distance = 10
    in_lat = lat_b
    in_lon = lon_b
    print("==== Checkpoint", count, " done ====\n")
    count += 1
    time.sleep(0.2)
    print("Start Moving to next checkpoint\n")
    time.sleep(1)

if __name__ == '__main__':
    
    try:
        main()
    except KeyboardInterrupt:
        print('Serial_STOP')
        #ser.write(str.encode('S'))
        raise Exception('Interrupt from keyboard...Program terminated.')
        exit()
        



