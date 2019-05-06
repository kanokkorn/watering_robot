#!/usr/bin/python3
import time
import keyboard
import logging
import argparse
from sys import platform

logging.basicConfig(
    filename="./_robot_log_.log",
    level=logging.DEBUG,
    format="[%(levelname)s]:[%(name)s]: %(message)s",
)
logger = logging.getLogger("Robot-Man")


# import serial

parser = argparse.ArgumentParser(description="Autonomous Robot")
# parser.add_argument('--port', '-p', type=str, required=True, help='Arduino port that connect to RPi')
# ser = serial.Serial( port, 9600)


def control():

    while True:
        try:
            if keyboard.is_pressed("w"):
                print("You Pressed Forward !")
                # ser.write(str.encode('M'))
                time.sleep(0.05)
                # finishing the loop

            elif keyboard.is_pressed("s"):
                print("You Pressed Backward !")
                # ser.write(str.encode('B'))
                time.sleep(0.05)

            elif keyboard.is_pressed("a"):
                print("You Pressed Left !")
                # ser.write(str.encode('L'))
                time.sleep(0.05)

            elif keyboard.is_pressed("d"):
                print("You Pressed Right !")
                # ser.write(str.encode('R'))
                time.sleep(0.05)

            elif keyboard.is_pressed("q"):
                print("You Pressed Quit !")
                logger.warning("Manual control stopped")
                # ser.write(str.encode('S'))
                time.sleep(0.05)
                break

            else:
                pass

        except:
            logger.warning("Manual control stopped")
            break


if __name__ == "__main__":
    logger.warning("Manual control started")
    control()
else:
    logger.warning("Manual control started")
    print("Manual Control Started")
    control()
