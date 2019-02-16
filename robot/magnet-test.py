import hashlib
import json
import smbus
import time
import math
import struct
import logging



logging.basicConfig(level=logging.INFO)
class compass(object):
    '''Interfaces to the hardware magnetometer (MAG3110) and
    works out which way we are pointing.
    '''
    def __init__(self):
        '''You knowns it
        '''
        self.heading            = 0
        self.busNumber          = 1
        self.calibrationFile    = 'compass.cal'
        self.addressCompass     = 0x0E
        # This is the raw min/max for calibration
        self.calibrations       = {'maxX':0,'minX':0,'maxY':0, 'minY':0, 'maxZ':0, 'minZ':0}
        # The offset is what is acutally applied to make it more accurate
        self.offset             = {'x':0, 'y':0, 'z':0}

        try:
            self.bus            = smbus.SMBus(self.busNumber)
        except Exception:
            logging.error('couldn\'t open bus: {0}'.format(e))
        #Init code taken from the XloBorg driver
        #https://www.piborg.org/xloborg

        bus                 = self.bus
        addressCompass      = self.addressCompass
        try:
            # read a byte to see if the i2c connection is working
            # disregared
            #pylint: disable=unused-variable
            byte = bus.read_byte_data(addressCompass, 1)
            logging.debug('Found compass at {0}'.format(addressCompass))
        except Exception:
            logging.error('Missing compass at {0} with error: {1}'.format(addressCompass))

        #warm up the compass
        register = 0x11             # CTRL_REG2
        data  = (1 << 7)            # Reset before each acquisition
        data |= (1 << 5)            # Raw mode, do not apply user offsets
        data |= (0 << 5)            # Disable reset cycle
        try:
            bus.write_byte_data(addressCompass, register, data)
        except Exception:
            logging.error('Failed sending CTRL_REG2: {0}'.format(e))

        # System operation
        register = 0x10             # CTRL_REG1
        data  = (0 << 5)            # Output data rate (10 Hz when paired with 128 oversample)
        data |= (3 << 3)            # Oversample of 128
        data |= (0 << 2)            # Disable fast read
        data |= (0 << 1)            # Continuous measurement
        data |= (1 << 0)            # Active mode
        try:
            bus.write_byte_data(addressCompass, register, data)
        except Exception:
            logging.error('Failed sending CTRL_REG1! {0}'.format(e))



    #pylint: disable=too-many-locals
    def rawMagnetometer(self):
        '''Return everything from the compass, once
        '''
        try:
            self.bus.write_byte(self.addressCompass, 0x00)
            #pylint: disable=unused-variable
            [status, xh, xl, yh, yl, zh, zl, who, sm, oxh, oxl, oyh, oyl, ozh, ozl, temp, c1, c2] = self.bus.read_i2c_block_data(self.addressCompass, 0, 18)
            bearings = struct.pack('BBBBBB', xl, xh, yl, yh, zl, zh)
            x, y, z = struct.unpack('hhh', bearings)


            #print self.bus.read_i2c_block_data(self.addressCompass, 0, 18)
        except Exception:
            logging.error('Unable to read compass: {0}'.format(e))
            return False

        return [x,y,z,temp]


    def calibrate(self):
        '''We need to calibrate the sensor
        otherwise we'll be going round in circles.

        basically we need to go round in circles and average out
        the min and max values, that is then the offset (?)
        https://github.com/kriswiner/MPU-6050/wiki/Simple-and-Effective-Magnetometer-Calibration

        Keep rotating the sensor in all direction until the output stops updating
        ctrl-c saves the calibration to a file
        '''
        calibrations = self.calibrations
        logging.info('Starting Debug, please roate the magnetomiter about all axis')
        start = True

        while True:
            try:
                change = False
                reading = self.rawMagnetometer()
                if start:
                    # get an initial reading, setting everything to zero means that the mimum
                    # only gets updated if it goes negative
                    calibrations['maxX'] = reading[0]
                    calibrations['minX'] = reading[0]
                    calibrations['maxY'] = reading[1]
                    calibrations['minY'] = reading[1]
                    calibrations['maxZ'] = reading[2]
                    calibrations['minZ'] = reading[2]
                    start = False

                # There must be a better way to do this, Perhaps dictonary iteration?

                # X calibration
                if reading[0] > calibrations['maxX']:
                    calibrations['maxX'] = reading[0]
                    change = True
                if reading[0]< calibrations['minX']:
                    calibrations['minX'] = reading[0]
                    change = True
                # Y calibrations
                if reading[1] > calibrations['maxY']:
                    calibrations['maxY'] = reading[1]
                    change = True
                if reading[1]< calibrations['minY']:
                    calibrations['minY'] = reading[1]
                    change = True
                # Z calibrations
                if reading[2] > calibrations['maxZ']:
                    calibrations['maxZ'] = reading[2]
                    change = True
                if reading[2]< calibrations['minZ']:
                    calibrations['minZ'] = reading[2]
                    change = True
                if change:
                    logging.info('Calibration Update:')
                    print (json.dumps(calibrations, indent=2))
                time.sleep(0.1)
            except KeyboardInterrupt:
                logging.debug('saving calibration')
                self.saveCalibration()
                return True

    def saveCalibration(self):
        '''Once calibrated we need to find a way to save it to the local file system
        '''
        try:
            with open(self.calibrationFile, 'w') as calibrationFile:
                calibration = json.dumps(self.calibrations, sort_keys=True)
                checksum = hashlib.sha1(calibration).hexdigest()
                calibrationFile.write(calibration)
                calibrationFile.write('\n')
                calibrationFile.write(checksum)
                calibrationFile.write('\n')
        except Exception:
            logging.error('unable to save calibration: {0}'.format(e))

    def loadCalibration(self):
        '''loads the json file that has the magic offsets in them
        Hopefully this will mean that it points within 15 degrees,
        '''
        try:
            with open(self.calibrationFile) as calibrationFile:
                calibration = calibrationFile.readline()
                checksum    = calibrationFile.readline()
        except Exception:
            logging.error('Unable to open com[ass calibration: {0}'.format(e))

        calibration = calibration.rstrip()
        checksum    = checksum.rstrip()
        if hashlib.sha1(calibration).hexdigest() == checksum:
            # we are good
            logging.debug('good calibrations')
            calibration = json.loads(calibration)
            print (calibration)
            self.calibrations = calibration
        else:
            logging.error('compass calibration file checksum mismatch')
            return False
        # http://www.bajdi.com/mag3110-magnetometer-and-arduino/
        self.offset['x'] = (calibration['minX'] + calibration['maxX'])/2
        self.offset['y'] = (calibration['minY'] + calibration['maxY'])/2
        self.offset['z'] = (calibration['minZ'] + calibration['maxZ'])/2


    def getBearing(self):
        '''Return a compass bearing in the form of 0-360
        '''
        reading = self.rawMagnetometer()
        # convert to raidians?
        # http://www.bajdi.com/mag3110-magnetometer-and-arduino/
        heading = math.atan2(reading[1] - self.offset['y'], reading[0] - self.offset['x'])
        if heading < 0:
            heading += 2 * math.pi
        return math.degrees(heading)


    def getCompenstatedBearing(self):
        '''Experiementally put roll and pitch back in to
        get some tilt compenstation
        https://gist.github.com/timtrueman/322555o
        roll    == x-z
        pitch   == y-z
        '''
        #first lets offset everything:
        raw = self.rawMagnetometer()
        x = raw[0] - self.offset['x']
        y = raw[1] - self.offset['y']
        z = raw[2] - self.offset['z']
        #I hope this is right...
        roll = math.atan2(x,z)
        pitch = math.atan2(y,z)
        compX = x * math.cos(pitch) + y * math.sin(roll) *math.sin(pitch) + z * math.cos(roll) * math.sin(pitch)
        compY = y * math.cos(roll) - z * math.sin(roll)
        heading = math.atan2(-compY, compX)
        if heading < 0:
            heading += 2 * math.pi
        return math.degrees(heading)

