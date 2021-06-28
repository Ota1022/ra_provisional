from bottle import Bottle,route,template,static_file,request,HTTPResponse,run
import simplejson as json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')


app = Bottle()
app.config['autojson'] = True


@app.route('/static/css/<filename:path>')
def send_static(filename):
    return static_file(filename, root=f'{STATIC_DIR}/css')

@app.route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./static')

@app.route('/static/image/<filename:path>')
def show_img(filename):
    return static_file(filename, root=f'{STATIC_DIR}/image/')

#JSONで送出する入力フォーム
@app.route('/data/json-form', method='GET')
def index():
    username = "Json Test Form"
    return template('form',username = username)

#JSONで受け取りJSONでレスポンスを返す。JSONエコー出力
@app.route('/data/json-get', method='POST')
def somethingjson():
    data = request.json
    #CORS対策
    header = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
    }
    ret = HTTPResponse(status=200, body=json.dumps(data,ensure_ascii=False, encoding='utf8', indent=2), headers=header)
    return ret

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="3000",debug=True)
