# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MAG3110
# This code is designed to work with the MAG3110_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Compass?sku=MAG3110_I2CS#tabs-0-product_tabset-2

import smbus
import time
import math

def __main__():
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

    if yMag > 0 :
        heading = 90 - math.atan2(xMag, yMag) * 180 / math.pi
    if yMag < 0 :
        heading = 270 - math.atan2(xMag, yMag) * 180 / math.pi
    if yMag == 0 & xMag < 0 : 
        heading = 180.0
    if yMag == 0 & xMag > 0 : 
        heading = 0.0

    # Output data to screen
    print ("Magnetic field in X-Axis : %d" %xMag)
    print ("Magnetic field in Y-Axis : %d" %yMag)
    print ("Magnetic field in Z-Axis : %d" %zMag)
    print ("Heading direction is :" + str(heading))


if __name__ == "__main__":
    for x in range(10000):
        __main__
        time.sleep(0.2)