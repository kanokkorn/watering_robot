from flask import Flask, render_template
import fwd.py
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('web-con.html')
@app.route('/background_process_test')
def background_process_test():
    fwd()
    return ("nothing")
if __name__ == '__main__':
    app.run(debug=True)