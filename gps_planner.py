import csv
import math
import time

#get lat lon from Ublox neo m6 via UART
def read_loc():
    with open('lat_lon.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            x = row[0]
            y = row[1]
            print(x, y)
            time.sleep(60)    
    return (x, y)
def distance():
    del_lat
    

    
def Deg_Rad(deg):
    rad = math.radians(deg)

    
    return rad
 read_loc()    