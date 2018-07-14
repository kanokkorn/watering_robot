import gps_planner, action, comm
import csv
import time


# read loc from csv file
def read_loc(lines):
    with open('lat_lon.csv') as f:
        lines = f.readlines()
    return(lines)
def action(act):
    if (lat_int == lat_fin) && (lon_int == lon_fin) :
        print("Agent is Watering")
        ser.write("Stop")
        time.sleep(10)
        pass
    if  (lat_int != lat_fin) && (lon_int != lon_fin) :
        print("Agent is moving")
        if () :
        ser.write("")
    
 
    
    