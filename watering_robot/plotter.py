import gps
import time
import threading
import os

class GPS_Poller(threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)    
      global session
      # Listen on port 2947 (gpsd) of localhost
      self.session = gps.gps(host="127.0.0.1",port="2947")
      self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
      self.stop_flag = False

   def get_speed(self):
      return self.session.fix.speed

   def get_location(self):
      return (self.session.fix.latitude,self.session.fix.longitude)

   def get_time(self):
      return self.session.utc

   def get_altitude(self):
      return self.session.fix.altitude

   def get_climb(self):
      return self.session.fix.climb

   def get_satellites(self):
      return self.session.satellites

   def run(self):
      global session
      while not self.stop_flag :
         try:
           self.session.next()
           #if you want to see how gpsd data look like uncomment 2 statements below and comment out a statement above.
           #report = self.session.next()
           #print report
         except KeyError:
           pass #nothing to do here
         except KeyboardInterrupt:
            self.session = None
            self.stop_flag = True
         except StopIteration:
            self.session = None
            print ("GPSD has terminated")
            self.stop_flag = True


if __name__ == "__main__" :
   gps_th = GPS_Poller()
   try :
      gps_th.start()
      while True :
         os.system('clear') #clear screen
         print 'Location ',gps_th.get_location()
         print 'Time ',gps_th.get_time()
         print 'Altitude ',gps_th.get_altitude()
         print 'Climb ',gps_th.get_climb()
         print 'Speed (m/s) ',gps_th.get_speed()
         print 'Satellites ',gps_th.get_satellites()
         time.sleep(2)
   except (KeyboardInterrupt, SystemExit):
      gps_th.stop_flag = True
      gps_th.join() # wait for the thread to finish it's job
