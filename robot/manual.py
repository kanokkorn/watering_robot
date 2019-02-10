import keyboard  # using module keyboard
import time
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

while True:  # making a loop
    
    try:  # used try so that if user pressed other than the given key error will not be shown
        
        if keyboard.is_pressed('w'):  # if key 'q' is pressed 
            print('You Pressed Forward !')
            ser.write(str.encode('M'))
            time.sleep(0.2)
              # finishing the loop
        
        elif keyboard.is_pressed('s'):  # if key 'q' is pressed 
            print('You Pressed Backward !')
            ser.write(str.encode('B'))
            time.sleep(0.2)
        
        elif keyboard.is_pressed('a'):  # if key 'q' is pressed 
            print('You Pressed Left !')
            ser.write(str.encode('L'))
            time.sleep(0.2)
            
        elif keyboard.is_pressed('d'):  # if key 'q' is pressed 
            print('You Pressed Right !')
            ser.write(str.encode('R'))
            time.sleep(0.2)
            
        elif keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed Quit !')
            ser.write(str.encode('S'))
            time.sleep(0.2)
            break
        
        else:
            pass
    except:
        
        ser.write(str.encode('S'))
        break