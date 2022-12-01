from flask import Flask, request, send_file
from flask_cors import CORS
from service import translate
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)
CORS(app)
@app.route('/')
def wwww():

    return "ww";




@app.route('/', methods = ['POST'])
def translateimage():
    f = request.files['file']
    f.save("./image/"+secure_filename(f.filename))
    filename='.\\image\\4844583611111.jpg'
    return send_file(filename,mimetype='image/jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=False)