import csv
import time
import pynmea2
import serial
import math as mth
import multiprocessing
#ser = serial.Serial ("/dev/ttyS0", 9600, timeout = 0.01)

def read_gps_csv():
    with open('watering_robot/lat_lon.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        geo_list = list(read_csv)
    return geo_list

def func_nmea_decode():
    
    pass

def func_gps_com():
    try:
        data = pynmea2.NMEAStreamReader(ser.readline())
        if data[0:6] == '$GPGGA':                
            msg = pynmea2.parse(data)
            print(msg.lat)
            print(msg.lon)
            com_list = [msg.lat, msg.lon]
            time.sleep(0.01)
            return com_list
    except:
        print("GPS signal not found")
        pass

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
# fixing 
def main():
    print(delta_lat(func_list_csv(),func_list_csv()))
    if func_list_csv() == func_list_com():
        print("Position matched. Start watering")
        #ser.writelines("S")
    else :
        print("Position not matched. Continues moving")
        #ser.writelines("M")
if __name__ == "__main__":
    main()