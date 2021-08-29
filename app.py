from qr import qrgen
from flask import  Flask,render_template, send_file, request
from flask import *

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/converted',methods = ['POST'])
def convert():
    global text
    text = request.form['test']
    return render_template('converted.html')

@app.route('/download',methods = ['GET'])
def download():
    qrgen(text)
    filename = text +'.png'
    return send_file(filename,as_attachment=True)

if __name__ == "__main__":
     app.run(debug=True)