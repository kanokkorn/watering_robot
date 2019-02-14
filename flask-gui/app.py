from flask import Flask, render_template
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('web-con.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    for i in range(3):
        ser.write(str.encode('M'))
        time.sleep(1)
    return render_template('web-con.html', message=forward_message);

if __name__ == '__main__':
    app.run(debug=True, host="172.16.173.2")