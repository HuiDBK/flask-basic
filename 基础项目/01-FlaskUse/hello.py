"""
@Author: Hui
@Desc: { flask框架初识使用 }
"""
from flask import Flask


# 创建flask应用
app = Flask(__name__)


# 创建视图函数
@app.route('/')
def index():
    return 'index page!'


@app.route('/hello')
def hello():
    return '<h1> Hello Flask! </h1>'


if __name__ == '__main__':
    # flask应用运行
    app.run()
