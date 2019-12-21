from flask import Flask, render_template
import serial
import time
#ser = serial.Serial('/dev/ttyUSB0', 9600)

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('web-con.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    for i in range(3):
        print("Moving forward "+str(i)+" sec")
        #ser.write(str.encode('M'))
        time.sleep(1)
    return render_template('fin.html');

@app.route("/backward/", methods=['POST'])
def move_backward():
    for i in range(3):
        print("Moving backward "+str(i)+" sec")
        #ser.write(str.encode('B'))
        time.sleep(1)
    return render_template('web-con.html');

@app.route("/left/", methods=['POST'])
def move_left():
    for i in range(3):
        print("Moving left "+str(i)+" sec")
        #ser.write(str.encode('L'))
        time.sleep(1)
    return render_template('web-con.html');

@app.route("/right/", methods=['POST'])
def move_right():
    for i in range(3):
        print("Moving right "+str(i)+" sec")
        #ser.write(str.encode('R'))
        time.sleep(1)
    return render_template('web-con.html');

@app.route("/stop/", methods=['POST'])
def move_stop():
    for i in range(3):
        print("Stopping...")
        #ser.write(str.encode('S'))
        time.sleep(1)
    return render_template('web-con.html');

if __name__ == '__main__':
    app.run(debug=True)
    #TODO: host='172.16.173.2' for raspberry pi