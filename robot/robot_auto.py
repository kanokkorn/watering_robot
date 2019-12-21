#!/usr/bin/python3
from sys import platform
import sys
import robot_network
import logging
import argparse
import time
import csv
import math

file_handler = logging.FileHandler(filename="./_robot_log_.log")
sys_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, sys_handler]

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s.%(msecs)03d]:[%(levelname)s]:[%(name)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=handlers,
)
logger = logging.getLogger("Robot-Auto")


def platform_chk():

    if platform == "linux" or platform == "linux2":

        logger.info("Platform detect : Linux")

    elif platform == "darwin":

        logger.info("Platform detect : MacOS")

    elif platform == "win32":

        logger.info("Platform detect : Windows")


def setup():
    ser = serial.Serial(port, 9600)
    gps_socket = gps3.GPSDSocket()
    data_stream = gps3.DataStream()
    gps_socket.connect()
    gps_socket.watch()
    logger.info("GPS & Arduino are set")
    pass


def test_and_carl():
    logger.debug("-- Testing Internet connection --")
    robot_network.network_test()
    time.sleep(3)
    logger.debug("-- Checking Validate GPS data")
    logger.info("Target " + str(csv_line()) + " checkpoints detected")
    logger.debug("-- Testing Sensor --")
    time.sleep(3)
    logger.debug("-- Testing GPS --")
    time.sleep(3)
    logger.debug("-- Test Complete --")
    pass


def initial():
    b = [0, 100]
    for i in range(csv_line()):
        logger.info("Checkpoint " + str(i))
        logger.info(str(csv_read()[i][0]) + "," + str(csv_read()[i][1]))
        distance = 10
        test_data_a = 10.712600
        test_data_b = 99.378650
        while distance > 5:
            distance = hsin(
                test_data_a,
                test_data_b,
                float(csv_read()[i][0]),
                float(csv_read()[i][1]),
            )
            print("{:0.2f} Meter".format(distance))
            test_data_a += 0.000005
            test_data_b += 0.000005
            time.sleep(0.05)
        b[0] = distance
        compara(b[0], b[1])
        b[1] = b[0]
        time.sleep(0.5)

    pass


def csv_line():
    file = open("./test-file.csv")
    numline = len(file.readlines())
    return numline


def csv_read():
    with open("./test-file.csv", newline="") as pos_file:
        read = csv.reader(pos_file)
        gps_list = list(read)
        return gps_list


def hsin(input_lat, input_lon, lat_des, lon_des):
    earth_radius = 6371e3
    lat_A = math.radians(input_lat)
    lat_B = math.radians(lat_des)
    del_lat = math.radians(lat_des - (input_lat))
    del_lon = math.radians(lon_des - (input_lon))
    a = (math.sin(del_lat / 2) * math.sin(del_lat / 2)) + math.cos(
        del_lat * math.cos(lat_B)
    ) * (math.sin(del_lon / 2) * math.sin(del_lon / 2))

    try:
        c = 2 * math.atan2(math.sqrt(a), math.sqrt((1 - a)))
    except ValueError:
        print("No Value")
    return earth_radius * c
    pass


def compara(x, y):
    if x > y:
        logger.warning("Distance is increasing ... Break engaged")
        exit()

if __name__ == "__main__":

    try:
        logger.info("<-- Initialize -->")
        platform_chk()
        test_and_carl()
        initial()
        logger.info("<-- Terminated -->")

    except KeyboardInterrupt:
        logger.critical("Keyboard interrupt!")
        raise Exception("Keyboard interrput from user. Control abort")
        exit()
else:
    try:
        logger.info("<-- Initialize -->")
        time.sleep(0.5)
        platform_chk()
        test_and_carl()
        logger.info(str(csv_read()))
        logger.info("<-- Terminated -->")

    except KeyboardInterrupt:
        raise Exception("Keyboard interrput from user. Control abort")
        logger.error("Keyboard interrupt!")
        exit()
