import csv
import math

#get lat lon from Ublox neo m6 via UART
def read_loc(lines):
    with open('lat_lon.csv') as f:
        lines = f.readlines()
        
    return(lines)
def haversine(lines):
    
    
    
def Deg_Rad(deg):
    rad = math.radians(deg)
    
    return rad
    
    