from flask import Flask, request
from flask_cors import CORS
from service import translate
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def hh():
    return json.dumps({'success' : True})

@app.route('/',methods=['POST'])
def hhhhh():
    params = json.loads(request.get_data())
    todoList={
        'id':1,
        'text':params['text'],
        'done':params['done'],
    }
    print(todoList)

    return json.dumps({'success' : True,'rep':todoList})

#@app.route('/', methods = ['POST'])
#def extract_highlight_times():
#    params = json.loads(request.get_data(), encoding='utf-8')
#    if len(params) == 0:
#        return json.dumps({'success' : False, 'time' : []})
#
 #  
 #   return json.dumps({'success' : True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, threaded=False)