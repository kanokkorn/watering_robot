from flask import Flask, render_template, Response
from video import Video

app = Flask(__name__)
vid = Video()

def gen():
    while True:
        frame = vid.cap_frame()
        yield(
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
        )

@app.route('/')
def video():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
     mimetype='multipart/x-mixed-replace; boundary=frame'
    )

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)