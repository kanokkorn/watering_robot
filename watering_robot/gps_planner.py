import csv
import math as m
import time

#get lat lon from Ublox neo m6 via UART
def read_files():
    with open('lat_lon.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            x = row[0]
            y = row[1]
            print(x, y)
            time.sleep(60)    
    return (x, y)
def distance():
    d_lat = m.log(m.tan(((m.pi)/4)+(lat_2/2))/m.tan(((m.pi)/4+lat_1/2) , base = e)
    q = d_la/d_lon
    d = m.sqrt((d_lat**2)+(q**2)*d)
    return ()
def crosstrack():
    
    return     
def Deg_Rad(deg):
    rad = math.radians(deg)    
    return rad
def mid_point():
    
    return 
def main():
    
    return
    
   