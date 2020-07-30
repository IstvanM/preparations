from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from redis import Redis
from rq import Queue
import os

redis = Redis(host='localhost', port=6379, db=0)
queue = Queue(connection=redis)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getenv('upload_path','/tmp/storage/')


@app.route('/')
def health_check():
    return 'OK'

@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    fname = secure_filename(f.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], fname)
    f.save(path)
    return f'Uploaded to:{path}'

@app.route('/list_uploaded')
def list_uploaded():
    path = app.config['UPLOAD_FOLDER']
    files_and_dirs = [f for f in os.listdir(path)]
    return files_and_dirs