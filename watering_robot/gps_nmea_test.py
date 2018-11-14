import gps3
the_connection = gps3.GPSDSocket() 
the_fix = gps3.Fix()
try:
    for new_data in the_connection:
        if new_data:
            the_fix.refresh(new_data)
        if not isinstance(the_fix.TPV['lat'], str): # lat as determinate of when data is 'valid'
            speed = the_fix.TPV['speed']
            latitude = the_fix.TPV['lat']
            longitude = the_fix.TPV['lon']
            altitude  = the_fix.TPV['alt']