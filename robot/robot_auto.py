#!/usr/bin/python3
from sys import platform
import logging
import argparse
import time
import csv

logging.basicConfig(
    filename="./_robot_log_.log",
    level=logging.DEBUG,
    format="[%(levelname)s]:[%(name)s]: %(message)s",
)
logger = logging.getLogger("Robot-Auto")


def arg_setup():
    parser = argparse.ArgumentParser(description="Autonomous Robot")
    parser.add_argument("--gps", "-g", type=str, required=True,
                        help="GPS file format .csv")
    parser.add_argument(
        "--port", "-p", type=str, required=True, help="Arduino port that connect to RPi"
    )


def platform_chk():

    if platform == "linux" or platform == "linux2":

        logger.info("Platform detect : Linux")

    elif platform == "darwin":

        logger.info("Platform detect : Linux")

    elif platform == "win32":

        logger.info("Platform detect : Windows")


def setup(port):
    ser = serial.Serial(port, 9600)
    gps_socket = gps3.GPSDSocket()
    data_stream = gps3.DataStream()
    gps_socket.connect()
    gps_socket.watch()
    logger.info("GPS & Arduino are set")
    pass


def test_and_carl():
    logger.debug("Testing Sensor")
    time.sleep(1)
    logger.debug("Testing GPS")
    time.sleep(1)
    logger.debug("Test Complete")
    time.sleep(1)
    pass


def initial():
    pass


def read_csv():
    with open("./robot/test-file.csv", newline="") as pos_file:
        read = csv.reader(pos_file)
        for gps_row in read:
            try:
                lat_des = float(gps_row[0])
                lon_des = float(gps_row[1])
                logger.info("GPS reading line...")
                return lat_des, lon_des
            except IndexError as err:
                raise Exception("GPS reading error")
                logger.error("GPS reading error")
                break
                


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


if __name__ == "__main__":

    try:
        arg_setup()
        logger.info("Started")
        time.sleep(0.5)
        platform_chk()
        test_and_carl()
        print(read_csv())
        logger.info("Ended")

    except KeyboardInterrupt:
        raise Exception("Keyboard interrput from user. Control abort")
        logger.error("Keyboard interrupt!")
        exit()
else:
    try:
        logger.info("Started")
        time.sleep(0.5)
        platform_chk()
        test_and_carl()
        logger.info("Ended")

    except KeyboardInterrupt:
        raise Exception("Keyboard interrput from user. Control abort")
        logger.error("Keyboard interrupt!")
        exit()
