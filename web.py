# -*- coding: utf-8 -*-
from flask import Flask  # 从Flask 引入flask
app = Flask(__name__)  # 这个应用的名称


@app.route('/')  # 装饰器，当flask收到和其参数相同的访问请求，将会执行它下面的代码
# 标准的函数，再往下就是返回体，你可以自定义
def index():
    return 'hello world, my hq'


# 再往下就是 app.run，可以定义端口与 ip。
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    # Internal Port 123, Port Forwarding 54.180.93.94:57850
    # http://54.180.93.94:57850/
