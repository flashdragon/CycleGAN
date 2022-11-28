from flask import Flask, request
from service import translate
import json

app = Flask(__name__)


@app.route('/', methods = ['POST'])
def extract_highlight_times():
    params = json.loads(request.get_data())
    if len(params) == 0:
        return json.dumps({'success' : False, 'time' : []})

    return json.dumps({'success' : True, 'time' : result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=False)