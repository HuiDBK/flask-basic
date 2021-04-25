"""
Author: hui
Desc: { Flask 路由分发 }
"""
from flask import Flask, url_for, redirect

app = Flask(__name__)


# app.route装饰器的作用是将路由映射到视图函数
@app.route("/hello")
def welcome():
    return "hello flask"


@app.route("/")
def index():
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    return "index page"


# 通过methods限定访问方式
@app.route("/post_only", methods=["POST"])
def post_only():
    return "post only page"


@app.route("/get_only", methods=["GET"])
def get_only():
    return "get only page"


@app.route("/test", methods=["GET", "POST"])
def test():
    return "post | get  page"


@app.route("/hi1")
@app.route("/hi2")
def hi():
    return "hi page"


@app.route("/login")
def login():
    # url = "/"
    # 使用url_for的函数，通过视图函数的名字找到视图对应的url路径
    url = url_for("welcome")
    print(url)
    return redirect(url)


@app.route("/register")
def register():
    url = "/"
    # url = url_for("index")
    return redirect(url)


if __name__ == "__main__":
    app.run()
