from flask import Flask, render_template
import fwd.py
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('web-con.html')
def contact():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            print("Start the process...")
            fwd()
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('contact.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)