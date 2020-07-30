from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from config import get_config
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = get_config('storage','upload_path')

@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    fname = secure_filename(f.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], fname)
    f.save(path)
    return f'Uploaded to: {path}'
    