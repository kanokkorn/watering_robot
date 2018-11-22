#import torch
import csv

with open('./watering_robot/lat_lon.csv', newline='') as f:
    read = csv.reader(f)
    for gps_row in read:
        print(gps_row)
        lat_b = float(gps_row[0]) #unpack list to float
        lon_b = float(gps_row[1]) 