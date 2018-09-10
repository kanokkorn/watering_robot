#from neo6 import GpsNeo6
import csv
import time
import pynmea2
#gps=GpsNeo6(port="/dev/ttyS0",debit=9600,diff=7) #diff is difference between utc time en local time    

def read_gps_csv():
    with open('watering_robot/lat_lon.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        geo_list = list(read_csv)
    return geo_list
def func_nmea_decode():
    pass
def func_gps_com():
    with open() as catread:
        #read_com = 
        com_list = list(read_com)
    func_nmea_decode()
    return com_list
def func_list_com():
    geo_list2x = read_gps_csv()
    geo_list = list(map(float, geo_list2x[1]))
    #gps.traite()
    print(geo_list[0],geo_list[1]) # print com list
    return geo_list[0],geo_list[1]

def func_list_csv():
    csv_list2x = read_gps_csv()
    csv_list = list(map(float, csv_list2x[1]))
    #gps.traite()
    print(csv_list[0],csv_list[1]) # print csv list
    return csv_list[0],csv_list[1]

if func_list_csv() == func_list_com():
    print("YEH BOI !1!1!!")
else :
    print("NAAAAAAA")