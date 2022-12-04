from flask import Flask, request, send_file
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from UGATIT import main
from werkzeug.utils import secure_filename
from db import MyImg
from PIL import Image
import base64
from io import BytesIO
import json

app = Flask(__name__)
CORS(app)


cnt=0
@app.route('/', methods = ['POST'])
def translateimage():
    global cnt
    f = request.files['file']
    f.save("./dataset/cat2emoticon/testA/"+secure_filename(f.filename))
    main.main()
    filename='./results/UGATIT_cat2emoticon_lsgan_4resblock_6dis_1_1_10_10_1000_sn_smoothing/'+secure_filename(f.filename)
    im=Image.open(filename)
    buffer=BytesIO()
    im.save(buffer,format='jpeg')
    img_str=base64.b64encode(buffer.getvalue())
    mysql=MyImg()
    mysql.insImg(cnt,img_str)
    cnt=cnt+1
    return send_file(filename,mimetype='image/jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=False)