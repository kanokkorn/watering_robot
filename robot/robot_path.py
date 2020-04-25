import logging
import time
import csv
import math

file_handler = logging.FileHandler(filename="./_robot_log_.log")
sys_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, sys_handler]

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s.%(msecs)03d]:[%(levelname)s]:[%(name)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=handlers,
)
logger = logging.getLogger("Robot-Auto")

def csv_line():
  try:
    file = open("./test-file.csv")
    numline = len(file.readlines())
    return numline
  except FileNotFoundError as err:
    logger.error('GPS file not found')

def csv_read():
  try:
    with open("./test-file.csv", newline="") as pos_file:
      read = csv.reader(pos_file)
      gps_list = list(read)
      return gps_list
  except FileNotFoundError as err:
    logger.error('GPS file not found')

def setup():
  try:
    ser = serial.Serial(port, 9600)
    gps_socket = gps3.GPSDSocket()
    data_stream = gps3.DataStream()
    gps_socket.connect()
    gps_socket.watch()
    logger.info("GPS & Arduino are set")
    return 1
  except Exception:
    logger.error("can't setup arduino, check cable and port?")
    return 0

def debug():
  pass

def release():
  pass

if __name__ == '__main__':
  logger.error('Must not called this file directly')
  exit()