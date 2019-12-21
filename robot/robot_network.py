import sys
import urllib.request
import logging

file_handler = logging.FileHandler(filename="./_robot_log_.log")
sys_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, sys_handler]

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)s]:[%(name)s]: %(message)s",
    handlers=handlers,
)
logger = logging.getLogger("Robot-Network")

def network_test():
    try:
        urllib.request.urlopen("https://google.com", timeout=0.5)
        logger.debug("Internet Connected")
        return True
    except urllib.request.URLError as err:
        logger.critical("Connection failed")
        raise Exception("Something's wrong with network")
        return False


if __name__ == "__main__":
    if network_test() == True:
        print("Network is working normally.")
    else:
        pass

