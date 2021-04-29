"""
Author: Hui
Desc: { Flask Cookie的使用 }
"""
from datetime import datetime, timedelta
from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    resp = make_response('success')

    resp.set_cookie("name", "hui")
    resp.set_cookie("age", "21")
    return resp


# 设置Cookie过期时间
@app.route("/set_expires")
def set_cookie_expires():
    resp = make_response("设置cookie过期时间")

    # 设置1分钟后过期
    resp.set_cookie("sex", "male", max_age=60)

    # 如果使用 expires，浏览器则会默认使用格林尼治时间
    # 即在设置的时间自动+8小时, 因此我们要减掉这8小时
    # datetime 对象在进行时间间隔运算不能直接 +- 要借助 timedelta

    # 设置一天后过期
    expires_date = datetime.now() + timedelta(days=1, hours=-8)
    resp.set_cookie("city", "GanZhou", expires=expires_date)

    return resp


@app.route("/get_cookie")
def get_cookie():
    name = request.cookies.get("name")
    age = request.cookies.get("age")

    resp = f"name={name}, age={age}"
    return resp


@app.route("/del_cookie")
def del_cookie():
    resp = make_response("del cookie")
    resp.delete_cookie("name")
    return resp


if __name__ == "__main__":
    app.run(debug=True)
