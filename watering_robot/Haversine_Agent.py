import csv
import time
from gps3 import gps3
import math as mth
import multiprocessing as multi

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

def read_gps_csv():
    with open('watering_robot/lat_lon.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        geo_list = list(read_csv)
    return geo_list

def func_gps_com():
    for new_data in gps_socket:
        if new_data:
            data_stream.unpack(new_data)
            print('Altitude = ', data_stream.TPV['alt'])
            print('Latitude = ', data_stream.TPV['lat'])
            

def func_list_com():
    geo_list2x = read_gps_csv()
    geo_list = list(map(float, geo_list2x[1]))
    print(geo_list[0],geo_list[1]) # print com list
    return geo_list[0],geo_list[1]

def func_list_csv(): # read .csv file
    csv_list2x = read_gps_csv()
    csv_list = list(map(float, csv_list2x[1]))
    print(csv_list[0],csv_list[1]) # print csv list
    return csv_list[0],csv_list[1]

def delta_lat(lat_csv,lat_com): # lat_com is initial, lat_csv is finish
    lat_csv = list(map(float, lat_csv[0]))
    lat_com = list(map(float, lat_com[0]))
    return(mth.log(mth.tan(((mth.pi)/4)+(((lat_com))/2))/mth.tan(((mth.pi)/4+((lat_csv))/2))))

def delta_lot(lon_csv,lon_com): # lon_com is initial, lon_csv is finish
    lon_csv = list(map(float, lon_csv[1]))
    lon_com = list(map(float, lon_com[1]))
    return(mth.log(mth.tan(((mth.pi)/4)+(lon_csv/2))/mth.tan(((mth.pi)/4+(lon_com/2)))))

def distance():
    delta_Q = ((delta_lat(func_list_csv(),func_list_csv())))/(delta_lot(func_list_csv(),func_list_csv()))
    earth_radius = 6371e3
    dstance = mth.sqrt(((delta_lat(func_list_csv(),func_list_csv()))**2)+(delta_Q**2)*earth_radius)
    return (dstance)

def bearing(lat_csv,lat_com):
    lat_csv = list(map(float, lat_csv[0]))
    lat_com = list(map(float, lat_com[0]))
    delta_Q = ((delta_lat(func_list_csv(),func_list_csv())))/(delta_lot(func_list_csv(),func_list_csv()))
    b_ring = mth.atan2(mth.sin(delta_Q)*mth.cos(lat_csv)*mth.cos(lat_com)*(mth.sin(lat_com)-mth.sin(lat_csv))*mth.cos(lat_csv)*mth.cos(delta_Q))
    return(b_ring)
# fixing 
def main_prog():
    #print(delta_lat(func_list_csv(),func_list_csv()))
    if func_list_csv() == func_list_com():
        print("Position matched. Start watering")
        print("Distance: "+distance()+"\nHeading: "+bearing(func_list_csv(),func_list_csv()))
        #ser.writelines("S")
    else :
        print("Position not matched. Continues moving")
        print("Distance: "+distance()+"\nHeading: "+bearing(func_list_csv(),func_list_csv()))
        #ser.writelines("M")
if __name__ == "__main__":
    process_1 = multi.Process(target=main_prog)
    process_2 = multi.Process(target=func_list_csv)
    process_1.start()
    process_2.start()