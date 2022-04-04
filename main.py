from os import abort
import requests
from flask import Flask, request
import flask_cors
import yaml
import json


ADDR_HOST = "0.0.0.0"
ADDR_PORT = 4561

app = Flask(__name__)
flask_cors.CORS(app, supports_credentials=True)

def _get(url):
    """
    获取配置文件 返回文本内容
    """
    r = requests.get(url)
    if r.status_code == 200:
        return r.text



@app.route("/api/sub", methods=['GET'])
def sub():
    sub_url = request.args.get("sub_url")
    replace_host = request.args.get("host")

    clash_config = _get(sub_url)
    if clash_config == None:
        abort(404)
    
    datas = yaml.load(clash_config, Loader=yaml.FullLoader)

    for index in range(len(datas["proxies"])):
        datas["proxies"][index]["ws-headers"]["Host"] = replace_host
    datas = yaml.dump(datas, allow_unicode=True)
    return datas

if __name__ == "__main__":
    app.run(ADDR_HOST, ADDR_PORT)