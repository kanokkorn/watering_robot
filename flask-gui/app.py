from flask import Flask, render_template
import fwd
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('web-con.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    fwd
    forward_message = "Moving Forward..."
    return render_template('web-con.html', message=forward_message);

if __name__ == '__main__':
    app.run(debug=True, host="172.16.173.2")