import serial
import sys, time
import comm
# global variable
j_val = ()

def forward():
    comm.ser("Forward")
    time.sleep(0.03)
    return
def backward():
    comm.ser("Backward")
    time.sleep(0.03)
    return
def left():
    comm.ser("Left")
    time.sleep(0.03)
    return
def right():
    comm.ser("Right")
    time.sleep(0.03)
    return
def main():
    if j_val < 0 & j_val >= -1:
        left()
        return
    elif j_val > 0 & j_val <= 1:
        right()
        return
    elif expression:
        pass
    elif expression:
        pass
# testing
main()

