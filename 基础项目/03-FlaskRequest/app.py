"""
Author: hui
Desc: { Flask request请求对象的使用 }
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    print('request.data', request.data)
    print('request.url', request.url)
    print('request.method', request.method)
    print('request.headers\n', request.headers)
    print('request.form', request.form)
    print('request.args', request.args)
    print('request.cookies', request.cookies)
    print('request.files', request.files)
    return 'Hello World!'


# 获取表单参数数据
@app.route('/index', methods=['GET', 'POST'])
def form_data():
    # request中包含了前端发送过来的所有请求数据
    # form和data是用来提取请求体数据
    # 通过request.form可以直接提取请求体中的表单格式的数据，是一个像字典的对象
    # 通过get方法只能拿到多个同名参数的第一个

    name = request.form.get('name')
    age = request.form.get('age')

    # 获取图片数据
    pic = request.files.get('pic')
    pic.save('./pic.png')

    name_li = request.form.getlist('name')
    res = 'name={}, age={}'.format(name_li, age)

    print('index')
    print(f'name={name}', f'age={age}')
    print(f'name_list={name_li}')
    return res


# 获取不是表单格式的数据，如 json、xml等
@app.route('/info', methods=['GET', 'POST'])
def raw_data():
    # 如果请求体数据不是表单格式的（如json格式），可以通过request.data获取
    res = request.data
    print(res)
    return res


# 获取查询字符串的参数数据
# http://127.0.0.1:5000/args?name=hui&age=21
@app.route('/args', methods=['GET', 'POST'])
def args_data():
    # 像字典对象一样使用
    name = request.args.get('name')
    age = request.args.get('age')
    res = f'name={name}, age={age}'
    print(res)
    return f'<h1> {res} </h1>'


if __name__ == '__main__':
    app.run()
