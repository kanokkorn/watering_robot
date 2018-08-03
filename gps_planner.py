import csv
import math

#get lat lon from Ublox neo m6 via UART
def read_loc():
    with open('lat_lon.csv') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
    pass
def haversine(lines):
    
    lat_int = 1
    lon_int = 0
    lat_fin = 1
    lon_fin = 0

    return lat_int, lat_fin, lon_int, lon_fin
    
def Deg_Rad(deg):
    rad = math.radians(deg)
    
    return rad
    
read_loc()    