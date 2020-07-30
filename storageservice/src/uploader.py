from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from config import get_config

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = get_config('storage','path')

@app.route('/upload', methods=['POST'])
def upload_file():
     if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
