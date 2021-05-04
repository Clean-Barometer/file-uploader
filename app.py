from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import base64
import os 

app = Flask(__name__)

@app.route('/')
def upload_f():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      print(base64.b64encode(f.read()))
      return 'file uploaded successfully'

# if __name__ == '__main__':
app.run(debug = True)
