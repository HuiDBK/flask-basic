"""
Author: Hui
Desc: { 了解 Flask 请求钩子 }
"""
from flask import Flask

app = Flask(__name__)


@app.route("/index")
def index():
    print("index called")
    a = 1 / 0
    response = '{"name": "hui"}'
    return response


@app.route("/hello")
def hello():
    print("hello called")
    return {'welcome': 'hello'}


@app.before_first_request
def handle_before_first_request():
    """
    在第一次请求处理之前先被执行
    """
    print("handle_before_first_request called")


@app.before_request
def handle_before_request():
    """
    在每次请求处理之前都被执行
    """
    print("handle_before_request called")


@app.after_request
def handle_after_request(response):
    """
    在每次请求处理之后被执行
    :param response: 视图函数处理之后返回的响应
    """
    print("handle_after_request called")
    # 指定响应返回格式类型为 json
    # response.headers['Content-Type'] = 'application/json'
    print(response)
    return response


@app.teardown_request
def handle_teardown_request(errors):
    """
    在每次请求处理之后都被执行，有没有异常都执行
    工作在非调试模式下（生产模式）
    :param: errors: 服务器出错的信息, 没有错误则为 None
    """
    print("handle_teardown_request called")
    print(errors)


if __name__ == "__main__":
    app.run()
