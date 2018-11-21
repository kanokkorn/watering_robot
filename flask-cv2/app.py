from flask import Flask
from camera import Camera

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

def 

if __name__ == "__main__":
    app.run(host='172.16.137.68', debug=True)