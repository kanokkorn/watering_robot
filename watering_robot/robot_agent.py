import asyncio
import time

async def setArduino(arduino_port):
  print('setting up Arduino')
  try:
    if arduino_port != 'tty/S0':
      print('port mismatched, check your connection')
      await asyncio.sleep(0.00001)
      return 0
    else:
      print('connected')
      await asyncio.sleep(0.00001)
      return 1
  except Exception as err:
    print('Some error occur, try again')
    return 0

async def readCSV():
  print('checking GPS path')
  gps_csv = True
  if gps_csv == True:
    print('gps setup complete')
    await asyncio.sleep(0.00001)
    return 1
  else:
    print('gps setup failed, check the file')
    return 0

async def setup_all():
  set_1 = setup.create_task(setArduino('tty/S0')) 
  set_2 = setup.create_task(readCSV())
  await asyncio.wait([set_1, set_2])

if __name__ == "__main__":
  setup = asyncio.get_event_loop()
  setup.run_until_complete(setup_all())
  setup.close()