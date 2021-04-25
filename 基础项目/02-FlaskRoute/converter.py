"""
@Author: Hui
@Desc: { flask框架的转换器练习 }
"""
from flask import Flask, url_for, redirect
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# str转换器 不加转换器类型， 默认是普通字符串规则（除了/的字符）
@app.route('/user/<username>')
def user_str(username):
    response = 'hello {}'.format(username)
    return response


# int转换器
@app.route('/user/<int:user_id>')
def user_int(user_id):
    response = 'hello {}'.format(user_id)
    return response


# path转换器
@app.route('/user/<path:user>')
def user_path(user):
    response = 'hello {}'.format(user)
    return response


# 自定义正则转换器
class RegexConverter(BaseConverter):
    """url正则匹配转换器"""

    def __init__(self, url_map, regex):
        super().__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        print("to_python() called...")
        print(f"value, {value}")
        # value是在路径进行正则表达式匹配的时候提取的参数
        # 留了一步处理提取出来参数
        # 这里返回值是最终解析的结果
        # return 'tel update 110'
        return value

    def to_url(self, value):
        """使用 url_for() 时调用"""
        # 可以改变 url_for() 处理的结果
        print("to_url() called...")
        print(f"value, {value}")
        # return "15811111111"
        return value


app.url_map.converters['re'] = RegexConverter

# 匹配手机号码的正则
MobileRegex = "'0?(13|14|15|17|18)[0-9]{9}'"


# 使用自定义的转换器
@app.route(f"/call/<re({MobileRegex}):tel>")
def call_tel(tel):
    response = 'tel: {}'.format(tel)
    return response


@app.route("/call")
def call():
    url = url_for('call_tel', tel='13577881658')
    print(f'url -> {url}')
    return redirect(url)


if __name__ == "__main__":
    app.run()
