"""
Author: Hui
Desc: { Flask session的使用 }
"""
from datetime import timedelta
from flask import Flask, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "it hui"

# 设置session过期时间
app.permanent_session_lifetime = timedelta(seconds=60)


# flask默认把session保存在cookie中
@app.route("/index")
def index():
    name = session.get("name")
    age = session.get("age")
    return f"name={name}, age={age}"


@app.route("/age")
def set_session():
    session["age"] = 21
    return "set session age"


@app.route("/login")
def login():
    session["name"] = "hui"
    # 开启session过期设置
    session.permanent = True
    return "set session name"


@app.route("del_session")
def del_session():
    session.pop("name")
    # session.clear() # 删除session所有信息
    return "del session name"


if __name__ == "__main__":
    app.run()
