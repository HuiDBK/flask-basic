# Flask 请求钩子

## 引言

> 在客户端和服务器交互的过程中，有些准备工作或扫尾工作需要处理，比如：
>
> - 在请求开始时，建立数据库连接
> - 在请求开始时，进行登陆权限认证
> - 在请求结束时，指定数据的交互格式
>
> **为了让每个视图函数避免编写重复功能的代码**，Flask 提供了通用设施的功能，即请求钩子。

<br/>

## Flask请求钩子

> 请求钩子是通过装饰器的形式实现，Flask支持如下四种请求钩子：

- `before_first_request: ` 在第一次请求处理之前先被执行
- `before_request: ` 在每次请求前执行，如果在某修饰的函数中返回了一个响应，视图函数将不再被调用
- `after_request: ` 在每次请求处理之后被执行
  - 接受一个参数：视图函数的响应
  - 在此函数中可以对响应值在返回之前做最后一步修改处理
  - 需要将参数中的响应在此参数中进行返回
- `teardown_request: ` 在每次请求后执行，接受一个参数：错误信息
  - 需要在非调式模式下运行

<br/>

## 代码测试

```python
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

```

<br/>

### 先访问 /hello

启动程序，先访问 `http://127.0.0.1:5000/hello` 

![访问/hello](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99f745470c9544dfa3fcbb7f14575a12~tplv-k3u1fbpfcp-watermark.image)

看看 `PyCharm` 输出的结果

```python
handle_before_first_request called	# Web应用第一次请求时

handle_before_request called	# 在每次请求前

hello called	# 视图函数打印的结果

handle_after_request called		# 在请求处理之后
<Response 20 bytes [200 OK]>

handle_teardown_request called
None	# 没有异常，打印的结果

127.0.0.1 - - [07/May/2021 23:32:25] "GET /hello HTTP/1.1" 200 -
```

<br/>

### 后访问 /index

然后再访问有 **除0异常** 的视图函数，`http://127.0.0.1:5000/index`

![访问/index](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7ed1ff9cd074bafb588fd67fd9af113~tplv-k3u1fbpfcp-watermark.image)

`PyCharm` 打印的结果

```python
handle_before_request called

index called	# 视图函数打印的结果

handle_after_request called
<Response streamed [500 INTERNAL SERVER ERROR]>

handle_teardown_request called
division by zero

[2021-05-07 23:32:40,479] ERROR in app: Exception on /index [GET]
```

<br/>

可以发现 `before_first_request` 请求钩子没有执行，它只会处理Flask应用程序的第一次的请求，之后的请求都不会执行这个请求钩子。

在出现异常情况的下 `after_request` 打印的响应结果，状态码 500 的服务器出错的响应，这个是Flask内置的一个响应结果。

而 `teardown_request` 则接受到了异常信息，输出了 `division by zero` 除0异常。

如果把 **调试模式 Debug mode** 打开，看看 `teardown_request` 是不是只运行在 非调试模式下

我们可以在 `PyCharm` 中编辑 `Flask` 配置信息

![编辑Flask配置信息](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95e32b90bb1d4ada805992ca4569f9bb~tplv-k3u1fbpfcp-watermark.image)

<br/>

![Flask配置](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d06bca65fcc46a79f24896bfe9817a2~tplv-k3u1fbpfcp-watermark.image)

<br/>

我这里开启了调试模式和指定了 IP和端口为 `127.0.0.1:8000` 

启动 `Flask` 程序再次访问 `http://127.0.0.1:8000/index`，网页显示如下

![调试模式下错误响应](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f14ab7d3935466d81cf0434abb7b653~tplv-k3u1fbpfcp-watermark.image)

<br/>

开启了调试模式，网页会输出具体错误信息。

然后再看看 `PyCharm` 输出结果

```python
handle_before_first_request called

handle_before_request called

index called

127.0.0.1 - - [08/May/2021 00:10:13] "GET /index HTTP/1.1" 500 -
```

<br/>

 `teardown_request` 请求钩子，没有执行，可以说明其工作在非调试模式下。

<br/>

## 源代码

源代码已上传到 `Gitee` [HuiDBK/FlaskBasic - 码云 - 开源中国 (gitee.com)](https://gitee.com/huiDBK/flask-basic/tree/master)，欢迎大家来访。

**✍ 码字不易，还望各位大侠多多支持❤️。**

<br/>

## 公众号
**<font size=4em color=#EE2178 >  新建文件夹X</font>**

> 大自然用数百亿年创造出我们现实世界，而程序员用几百年创造出一个完全不同的虚拟世界。我们用键盘敲出一砖一瓦，用大脑构建一切。人们把1000视为权威，我们反其道行之，捍卫1024的地位。我们不是键盘侠，我们只是平凡世界中不凡的缔造者 。