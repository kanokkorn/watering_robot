import gps_planner, action, comm



# read loc from text file
def read_loc(lines):
    with open('lat_lon.txt') as f:
        lines = f.readlines()
    return(lines)
