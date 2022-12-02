from flask import Flask, request, send_file
from flask_cors import CORS
from UGATIT import main
from service import translate
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)
CORS(app)


@app.route('/', methods = ['POST'])
def translateimage():
    f = request.files['file']
    print(f.filename)
    f.save("./dataset/cat2emoticon/testA/"+secure_filename(f.filename))
    main.main()
    filename='./results/UGATIT_cat2emoticon_lsgan_4resblock_6dis_1_1_10_10_1000_sn_smoothing/'+secure_filename(f.filename)
    return send_file(filename,mimetype='image/jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=False)