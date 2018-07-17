import serial
import sys, os
import math

#get lat lon from Ublox neo m6 via UART
def haversine(lines):
    lat_int = 1
    lon_int = 0
    lat_fin = 1
    lon_fin = 0



    return lat_int, lat_fin, lon_int, lon_fin
    
def Deg_Rad(deg):
    rad = math.radians(deg)
    return rad
    
    