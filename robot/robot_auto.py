#!/usr/bin/python3
from sys import platform
import logging
import argparse
import time

parser = argparse.ArgumentParser(description="Autonomous Robot")
parser.add_argument("--gps", "-g", type=str, required=True, help="GPS file format .csv")
parser.add_argument(
    "--port", "-p", type=str, required=True, help="Arduino port that connect to RPi"
)
logging.basicConfig(
    filename="./_robot_log_.log",
    level=logging.DEBUG,
    format="[%(levelname)s]:[%(name)s]: %(message)s",
)
logger = logging.getLogger("Robot-Auto")


def platform_chk():

    if platform == "linux" or platform == "linux2":

        logger.info("Platform detect : Linux")

    elif platform == "darwin":

        logger.info("Platform detect : Linux")

    elif platform == "win32":

        logger.info("Platform detect : Windows")


def _setup_(port):
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


def _initial_():
    pass


def _hsin_():
    pass


if __name__ == "__main__":

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
