"""
Author: hui
Desc: { Flask response响应的练习 }
"""
import json
from flask import abort, redirect, request
from flask import Flask, make_response, jsonify

app = Flask(__name__)


# 以元组形式返回响应信息
@app.route("/index")
def index():
    header_dict = {
        "name": "jack",
        "age": 22
    }

    header_list = [("name", "hui"), ("age", 21)]

    header_dict = {
        "Content-Type": " text/html; charset=utf-8",  # 响应返回的数据类型
        "Cookie": "name=hui; age=21"  # 响应设置cookie
    }

    #      响应体        状态码    响应头
    return "index page", 400, header_dict
    # return "index page", 400, header_list


# mk_response 设置响应信息
@app.route("/info")
def info():
    resp = make_response("info page")
    resp.status = "666 ithui"
    resp.headers["name"] = "hui"
    resp.headers["age"] = 21
    return resp


# jsonify 返回json数据
@app.route("/json")
def resp_json():
    data = {
        "name": "hui",
        "age": 21
    }

    # json_str = json.dumps(data)
    # headers = {"Content-Type": "application/json"}
    # return json_str, 200, headers

    return jsonify(data)
    # return jsonify(name="jack", age=20)


# 自己设置重定向信息
@app.route('/baidu')
def red_baidu():
    resp = make_response()
    resp.status = "302"
    resp.headers['Location'] = "http://www.baidu.com"
    return resp


# redirect 响应重定向
@app.route("/csdn")
def red_csdn():
    csdn_url = "https://blog.csdn.net/qq_43629857"
    return redirect(csdn_url)


# 处理404状态错误
@app.errorhandler(404)
def handle_404_err(err):
    return f"404 错误信息 {err}"


# 处理500状态错误
@app.errorhandler(500)
def handle_500_err(err):
    return f"500 服务器错误 {err}"


# abort中断
# http://127.0.0.1:5000/login?name=hui&pwd=123
@app.route("/login", methods=['GET'])
def login():
    name = request.args.get("name")
    pwd = request.args.get("pwd")
    if name != "hui" or pwd != "123":
        abort(404)

    return "登录成功"


if __name__ == "__main__":
    app.run()
