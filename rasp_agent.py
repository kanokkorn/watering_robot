#import gps_planner, action, 
import comm
import csv
import time


# read loc from csv file

def action(lat_int, lat_fin, lon_int, lon_fin):
    if (lat_int == lat_fin) & (lon_int == lon_fin) :
        print("Agent is Watering")
        ser.write("Stop")
        time.sleep(10)
        pass
    if  (lat_int != lat_fin) & (lon_int != lon_fin) :
        print("Agent is moving")
        ser.write("Forward")
        time.sleep(3)
        pass
    
def main():
    #haversine(lines)
    comm.serial("hello")

    pass
while 1:
    main()
 
    
    