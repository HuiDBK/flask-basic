# Flask response响应

## 引言

> 客户端发送 `http` 请求给 Flask程序，Flask 调用视图函数后，会将其返回值作为响应的内容。大多情况下，响应就是一个简单的字符串，作为 Html 页面回送客户端。
>
> 但 `http` 协议需要的不仅是作为请求响应的字符串。`http` 响应中有一个很重要的部分是状态码，Flask设为200，代表请求已被成功处理。

<br/>

## response响应

### 元组形式响应

如果视图函数返回的响应还需要使用不同的状态码，那么可以把数字代码作为第二个返回值，添加到响应文本之后

```python
from flask import Flask

app = Flask(__name__)


# 以元组形式返回响应信息
@app.route("/index")
def index():
    #      响应体        状态码
    return "index page", 400
```

<br/>

视图函数返回的响应还可以接受第三个参数，响应头也可以继续放在后面返回，例如：

```python
from flask import Flask


app = Flask(__name__)


# 以元组形式返回响应信息
@app.route("/index")
def index():
    header_dict = {
        "name": "jack",
        "age": 22
    }

    header_list = [("name", "hui"), ("age", 21)]

    #      响应体        状态码    响应头
    return "index page", 400, header_dict
    # return "index page", 400, header_list
    
```

<br/>

但响应头信息要用一个字典或列表包装起来，字典好理解，列表里面则是以元组形式存储响应头信息。这里返回的只是做个例子，真正返回的时候，要合理设置响应头信息，例如 

```python
header_dict = {
    "Content-Type": " text/html; charset=utf-8",# 响应返回的数据类型
    "Set-Cookie": "name=hui; Path=/"    			# 响应设置cookie
}
return "index page", 200, header_dict   
```

<br/>

浏览器开发者工具查看响应信息

![查看响应体信息](https://img-blog.csdnimg.cn/20210428200713254.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

**切记：以元组形式返回，位置不能够乱，返回值**

- 第一个对应响应体
- 第二个对应状态码
- 第三个对应响应头

<br/>

### make_response函数

> 如果不想返回由1个、2个或3个值组成的元组，Flask视图函数还可以返回 Response 对象。`make_response` 函数可接受1个、2个或3个参数（和视图函数的返回值一样），并返回一个Response对象。看看到底如何使用

<br/>

```python
from flask import Flask, make_response

app = Flask(__name__)

# mk_response 设置响应信息
@app.route("/info")
def info():
    resp = make_response("info page")
    resp.status = "666 ithui"
    resp.headers["name"] = "hui"
    resp.headers["age"] = 21
    return resp
```

<br/>

**注意：`make_response()` 对象设置状态码时必须字符串，不要写成了数字**

<br/>

### 返回json格式数据

```python
import json
from flask import Flask, make_response

app = Flask(__name__)


@app.route("/json")
def resp_json():
    data = {
        "name": "hui",
        "age": 21
    }

    json_str = json.dumps(data)
    headers = {"Content-Type": "application/json"}
    return json_str, 200, headers
```

你可以借助 `json` 模块进行数据 json化，但一般返回json数据要设置前端返回的数据类型，Flask默认的是`text/html`，因此我们还需在单独设置响应体内容类型。

由于json格式数据在Web开发中使用频繁，在 `Flask` 中专门提供了 `jsonify()` 函数进行 json数据的响应

具体使用如下

```python
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/json")
def resp_json():
    data = {
        "name": "hui",
        "age": 21
    }
    return jsonify(data)
    # return jsonify(name="jack", age=20)
```

`jsonify()`可以接收一个字典，也可以 `key-value` 形式来构造 `json` 数据。这样就方便许多

<br/>

## 其他特殊响应

### redirect() 重定向

> 有一种名为重定向的特殊响应类型。这种响应类型没有页面文档，只告诉浏览器一个新地址用以加载新页面

```python
from flask import Flask, redirect

app = Flask(__name__)

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
```

重定向的经常使用 `302` 状态码表示，指向的地址由 `Location` 首部提供。由于使用频繁，`Flask` 提供了辅助函数 `redirect()`，用于生成这种响应。

<br/>

### abort() 中断

abort()接收一个状态码参数

```python
from flask import Flask, request, abort

app = Flask(__name__)

# abort中断
# http://127.0.0.1:5000/login?name=hui&pwd=123
@app.route("/login", methods=['GET'])
def login():
    name = request.args.get("name")
    pwd = request.args.get("pwd")
    if name != "hui" or pwd != "123":
        abort(404)

    return "登录成功"
```

<br/>

一般这个 `abort()` 函数都会配合错误信息处理装饰器 `app.errorhandler()` 一起使用，如下：

```python
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
```

<br/>

## 源代码

源代码已上传到 `Gitee` [HuiDBK/FlaskBasic - 码云 - 开源中国 (gitee.com)](https://gitee.com/huiDBK/flask-basic/tree/master)，欢迎大家来访。

**✍ 码字不易，还望各位大侠多多支持❤️。**

<br/>

## 公众号
**<font size=4em color=#EE2178 >  新建文件夹X</font>**

> 大自然用数百亿年创造出我们现实世界，而程序员用几百年创造出一个完全不同的虚拟世界。我们用键盘敲出一砖一瓦，用大脑构建一切。人们把1000视为权威，我们反其道行之，捍卫1024的地位。我们不是键盘侠，我们只是平凡世界中不凡的缔造者 。