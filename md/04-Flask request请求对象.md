# Flask request请求对象

## 引言

> 客户端发送 `http` 请求给 Flask程序，都会携带一些对应的请求信息，该如何获取呢？

```python
from flask import request
```

`request` ，就是 Flask 中表示当前请求的对象，`request` 对象中保存了一次 `http` 请求的所有数据，并进行了封装处理，我们就可以用这个 `request` 请求对象来获取请求信息。

<br/>

## request常用属性

| 属性      | 说明                              |
| --------- | --------------------------------- |
| `data`    | 记录请求的数据，如 `json、xml` 等 |
| `form`    | 记录请求中的表单数据              |
| `args`    | 记录请求中的查询参数              |
| `cookies` | 记录请求中的 `cookie` 信息        |
| `headers` | 记录请求中的报文头                |
| `method`  | 记录请求中的请求方式              |
| `url`     | 记录请求的 `URL` 地址             |
| `files`   | 记录请求上传的文件                |

<br/>

接下来就挨个用一下。

```python
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

```

<br/>

访问 `http://127.0.0.1:5000/` 后PyCharm终端显示的结果如下

```python
127.0.0.1 - - [26/Apr/2021 20:21:03] "GET / HTTP/1.1" 200 -
request.data b''

request.url http://127.0.0.1:5000/
        
request.method GET

request.headers
Host: 127.0.0.1:5000
    Connection: keep-alive
    Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"
    Sec-Ch-Ua-Mobile: ?0
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.42
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Sec-Fetch-Site: none
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
    Cookie: csrftoken=XjZW5a3obvzYxm5dqYtdsWRS5GzVP4tHMJTNquEVJVdWknIJXwRMaTJKYfOTCojh; Hm_lvt_b64a44bf14fabebd68d595c81302642d=1618121686,1618130897,1618133833,1618134629


request.form ImmutableMultiDict([])
request.args ImmutableMultiDict([])
request.cookies ImmutableMultiDict([('csrftoken', 'XjZW5a3obvzYxm5dqYtdsWRS5GzVP4tHMJTNquEVJVdWknIJXwRMaTJKYfOTCojh'), ('Hm_lvt_b64a44bf14fabebd68d595c81302642d', '1618121686,1618130897,1618133833,1618134629')])
request.files ImmutableMultiDict([])

```

<br/>

### 获取表单参数

> 首先要构建表单数据中，可以自己写一个网页，也可以用 `PostMan` 工具，这里是用 `PostMan` 来测试
>
> `PostMan` 工具官网下载 [https://www.postman.com/downloads/](https://www.postman.com/downloads/)
>
> `PostMan` 工具使用教程可以参考文章 [Postman使用详解](https://blog.csdn.net/fxbin123/article/details/80428216)

<br/>

**PostMan构建请求及数据**

![PostMan发送表单数据](https://img-blog.csdnimg.cn/20210426210330974.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

**编写视图函数**

```python
from flask import Flask, request

app = Flask(__name__)

# 获取表单参数数据
@app.route('/index', methods=['GET', 'POST'])
def form_data():

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
```

<br/>

`PyCharm` 终端展示详情

![PyCharm展示结果](https://img-blog.csdnimg.cn/20210426211438514.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

`form` 是用来提取请求体数据

通过 `request.form` 可以直接提取请求体中的表单格式的数据，是一个像字典的对象

通过 `get` 方法只能拿到多个同名参数的第一个， `getList` 才可以获取全部。

<br/>

### 获取查询字符串参数

**编写视图函数**

```python
from flask import Flask, request

app = Flask(__name__)

# 获取查询字符串的参数数据
# http://127.0.0.1:5000/args?name=hui&age=21
@app.route('/args', methods=['GET', 'POST'])
def args_data():
    name = request.args.get('name')
    age = request.args.get('age')
    res = f'name={name}, age={age}'
    print(res)
    return f'<h1> {res} </h1>'
```

<br/>

![查询字符串参数获取](https://img-blog.csdnimg.cn/20210426213059753.png)

`PyCharm` 终端显示的信息

```python
name=hui, age=21
127.0.0.1 - - [26/Apr/2021 21:33:55] "GET /args?name=hui&age=21 HTTP/1.1" 200 -
```

<br/>

### 获取其他格式数据

> 获取前端发送过来的 `json、xml` 等数据

<br/>

**编写视图函数**

```python
from flask import Flask, request

app = Flask(__name__)

# 获取不是表单格式的数据，如 json、xml等
@app.route('/info', methods=['GET', 'POST'])
def raw_data():
    # 如果请求体数据不是表单格式的（如json格式），可以通过request.data获取
    res = request.data
    return res
```

<br/>

**PostMan构造请求查看**
![PostMan发送Json数据](https://img-blog.csdnimg.cn/20210426214009815.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)
<br/>
![PostMan发送xml数据](https://img-blog.csdnimg.cn/20210426214212615.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

## request对象知识扩展

> 我们在每一个视图函数中都使用这同一个 `request` 请求对象，像当全局变量一样使用。事实上，request 不可能是全局变量。试想，在多线程服务器中，多个线程同时处理不同客户端发送的不同请求时，每个线程看到的 request 对象必然不同。

在 `Django` 中则是让每个请求让视图函数以参数的形式进行保存，以致区分不同请求，而 `Flask` 则是通过使用上下文让特定的变量在一个线程中全局可访问，与此同时却不会干扰其他线程。

可以了解一下 **线程局部变量 Thread Local** 概念，大致实现方式

```python
ThreadLocal{
    "线程A": {
        args: {'name': 'hui', 'age': 21},
        data: "{"name": "hui", "age": "21"}",	# 假设json字符串
        form: {'name': 'hui', 'age': 21}
        ...其他数据
    },
    
    "线程B": {
        args: {'name': 'jack', 'age': 22},
        data: "{"name": "jack", "age": "22"}",
        form: {'name': 'jack', 'age': 22}
        ...其他数据
    },
    
	......其他线程
}

request = ThreadLocal.get("线程名")
```

Flask先在视图函数中有请求上下文环境，它会根据运行在哪一个线程，去取相对应线程的请求数据。

![线程局部变量](https://img-blog.csdnimg.cn/20210426230238529.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

## 源代码

源代码已上传到 `Gitee` [HuiDBK/FlaskBasic - 码云 - 开源中国 (gitee.com)](https://gitee.com/huiDBK/flask-basic/tree/master)，欢迎大家来访。

**✍ 码字不易，还望各位大侠多多支持:heart:。**

<br/>

## 公众号
**<font size=4em color=#EE2178 >  新建文件夹X</font>**

> 大自然用数百亿年创造出我们现实世界，而程序员用几百年创造出一个完全不同的虚拟世界。我们用键盘敲出一砖一瓦，用大脑构建一切。人们把1000视为权威，我们反其道行之，捍卫1024的地位。我们不是键盘侠，我们只是平凡世界中不凡的缔造者 。