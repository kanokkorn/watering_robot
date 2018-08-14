import csv, time
import math as m
import pynmea2 as nm2
import gpsd

# get lat lon from Ublox neo m6 via UART
def Ublox():
    ublox_d = nm2.parse(gps_in)
    return((ublox_d.latitude),(ublox_d.longitude))
# get lat and long from .csv files
def read_files():
    with open('watering_robot/lat_lon.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        geo_list = list(readCSV)
    return (geo_list)
# calculate heading direction
def bearing():

    pass
# calculate distance between two points
def distance():
    q = (delta_lat())/(delta_lot)
    d = m.sqrt((d_lat**2)+(q**2)*d)
    return ()
# delta latitude
def delta_lat(lat_1, lat_2):
    return(m.log(m.tan(((m.pi)/4)+(lat_2/2))/m.tan(((m.pi)/4+(lat_1/2)))))
# delta longtitude
def delta_lot(lot_1, lot_2):
    return(m.log(m.tan(((m.pi)/4)+(lot_2/2))/m.tan(((m.pi)/4+(lot_1/2)))))

#print(delta_lat(69.09, 87.65))
geo_list2x = read_files()
geo_list = list(map(float, geo_list2x[1]))
print(delta_lat(float(geo_list[0]), float(geo_list[0])))
for 
    # loop goes here
    try:
        
        pass
    except ValueError:
        print("Get value error ! maybe it's end of file")
        raise SystemExit
    finally:
        pass
