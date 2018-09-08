from neo6 import GpsNeo6

gps=GpsNeo6(port="/dev/ttyS0",debit=9600,diff=7) #diff is difference between utc time en local time    

def read_files():
    with open('watering_robot/lat_lon.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        geo_list = list(readCSV)
    return (geo_list)

while 1:
    geo_list2x = read_files()
    geo_list = list(map(float, geo_list2x[1]))
    #gps.traite()
    print(geo_list) # print all info
    #print(gps.latitude,gps.longitude)
