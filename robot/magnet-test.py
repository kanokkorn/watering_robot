# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MAG3110
# This code is designed to work with the MAG3110_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Compass?sku=MAG3110_I2CS#tabs-0-product_tabset-2

import smbus
import time
import os
import math

def magnet_test():

    x_axis = [0, 1]
    y_axis = [0, 1]
    z_axis = [0, 1]
    # Get I2C bus
    bus = smbus.SMBus(1)

    # MAG3110 address, 0x0E(14)
    # Select Control register, 0x10(16)
    #		0x01(01)	Normal mode operation, Active mode
    bus.write_byte_data(0x0E, 0x10, 0x01)

    time.sleep(0.5)

    # MAG3110 address, 0x0E(14)
    # Read data back from 0x01(1), 6 bytes
    # X-Axis MSB, X-Axis LSB, Y-Axis MSB, Y-Axis LSB, Z-Axis MSB, Z-Axis LSB
    data = bus.read_i2c_block_data(0x0E, 0x01, 6)
    # Convert the data
    xMag = data[0] * 256 + data[1]
    if xMag > 32767 :
    	xMag -= 65536

    yMag = data[2] * 256 + data[3]
    if yMag > 32767 :
    	yMag -= 65536

    zMag = data[4] * 256 + data[5]
    if zMag > 32767 :
    	zMag -= 65536
    
    x_axis[0] = xMag
    y_axis[0] = yMag
    z_axis[0] = zMag
    
    if x_axis[0] > x_axis[1]:
        x_axis[1] = x_axis[0]
    else:
        pass

    if y_axis[0] > y_axis[1]:
        y_axis[1] = y_axis[0]
    else:
        pass
    
    if z_axis[0] > z_axis[1]:
        z_axis[1] = z_axis[0]
    else:
        pass

    try: 
        avg_x = (x_axis[1] - x_axis[0])/2
        avg_y = (y_axis[1] - y_axis[0])/2
        avg_z = (z_axis[1] - z_axis[0])/2

        off_x = (x_axis[1] + x_axis[0])/2
        off_y = (y_axis[1] + y_axis[0])/2
        off_z = (z_axis[1] + z_axis[0])/2

        delta_avg = (avg_x + avg_y + avg_z)/3

        scale_x = delta_avg / avg_x
        scale_y = delta_avg / avg_y
        scale_z = delta_avg / avg_z

        correct_x = (xMag - off_x) * scale_x
        correct_y = (yMag - off_y) * scale_y
        correct_z = (zMag - off_z) * scale_z
    
    except ZeroDivisionError:

        correct_x = 2
        correct_y = 3
        print("Division by zero")
        pass

    mag_angle = math.degrees(math.atan2(correct_y, correct_x))

    os.system('cls||clear')
    print ("Magnetic field in X-Axis : %d" %correct_x)
    print ("Magnetic field in Y-Axis : %d" %correct_y)
    print ("Magnetic field in Z-Axis : %d" %correct_z)

    print("\nAngle: %d" %mag_angle)

if __name__ == "__main__":
    
    #test for 100 times
    for x in range(10000):
        magnet_test()
        time.sleep(0.2)

    exit()
