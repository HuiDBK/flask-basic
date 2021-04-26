# Flask路由分发及转换器

## 引言

> 本文重点介绍，Flask路由分发及访问静态资源。

<br/>

## 路由分发

> `app.route` 装饰器的作用是将路由映射到视图函数，从浏览器输入对应的 `url` 地址，Flask程序，就会根据 `url` 找到对应的视图函数`(View Function)`  进行处理。视图函数名字可以与 `url` 不同。`route` 装饰器内部会调用`add_url_route()` 方法实现路由注册。

```python
"""
Author: hui
Desc: { Flask 路由分发 }
"""
from flask import Flask, url_for, redirect

"""
# 创建flask的应用对象
# __name__表示当前的模块名字
"""
app = Flask(__name__)


@app.route("/hello")
def welcome():
    return "hello flask"


@app.route("/index")
def index():
    return "index page"


if __name__ == "__main__":
    app.run()
    
```

<br/>

### 给路由指定访问方式

> 通过 `methods` 限定访问方式， 接受参数形式为列表

```python
# post
@app.route("/post_only", methods=["POST"])
def post_only():
    return "post only page"


# get
@app.route("/get_only", methods=["GET"])
def get_only():
    return "get only page"

# post or get
@app.route("/test", methods=["GET", "POST"])
def test():
    return "post | get  page"
```

<br/>

### 多个路由绑定同一视图函数

```python
@app.route("/hi1")
@app.route("/hi2")
def hi():
    return "hi page"
```

访问这两个`/hi1`，`/hi2`路径显示的效果都是 `hi page`

![多个路由绑定到同一视图函数](https://img-blog.csdnimg.cn/20210425143423325.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

### url_for()和redirect()

> 使用 `url_for()` 的函数，可以通过 **视图函数的名字** 找到视图对应的 `url` 路径
>
> 而 `redirect()` 函数则是 `url` 重定向，会再次发送一个新的请求。
>
> 从 `flask` 库中导入这两个函数，一般这两个函数会一起使用。

<br/>

```python
from flask import Flask, url_for, redirect


app = Flask(__name__)


# app.route装饰器的作用是将路由映射到视图函数
@app.route("/hello")
def welcome():
    return "hello flask"


@app.route("/")
def index():
    return "index page" 


@app.route("/login")
def login():
    # url = "/hello"
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

```

<br/>

```python
url_for('welcome') 等同于 /hello
url_for('index') 等同于 /
```

<br/>

在测试功能前，首先在浏览器中，右击鼠标选择检查或 `F12` 打开浏览器调试工具。进入 `NetWork` 选项。

![浏览器调试工具](https://img-blog.csdnimg.cn/20210425151308265.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

然后在网址栏上分别输入 `http://127.0.0.1:5000/login` 和`http://127.0.0.1:5000/register` 

![redirect请求重定向](https://img-blog.csdnimg.cn/2021042515221717.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

这里就展示访问 `/login` 的效果，可以发现直接跳转到了 `/hello` 。这就是 **重定向**，发送了两次请求。

然后再看看 `PyCharm` 运行 `Flask` 程序的信息。

 ```python
127.0.0.1 - - [25/Apr/2021 15:09:34] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [25/Apr/2021 15:18:25] "GET /login HTTP/1.1" 302 -
/hello
127.0.0.1 - - [25/Apr/2021 15:18:25] "GET /hello HTTP/1.1" 200 -
127.0.0.1 - - [25/Apr/2021 15:29:05] "GET /register HTTP/1.1" 302 -
127.0.0.1 - - [25/Apr/2021 15:29:05] "GET / HTTP/1.1" 200 -
 ```

**切记**：`url_for()` 接收的是 **视图函数的名称**，返回的是对应的 `url` 路径，切勿把 `url` 路径传进去。 

<br/>

### 查看全部路由信息

> 通过 `app.url_map` 可以查看所有路由信息

```python
"""
Author: hui
Desc: { Flask 路由分发及静态资源访问 }
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


# 其他视图函数省略...


if __name__ == "__main__":
    app.run()

```

<br/>

访问首页打印如下结果

```python
Map([<Rule '/post_only' (OPTIONS, POST) -> post_only>,
 <Rule '/get_only' (OPTIONS, HEAD, GET) -> get_only>,
 <Rule '/register' (OPTIONS, HEAD, GET) -> register>,
 <Rule '/hello' (OPTIONS, HEAD, GET) -> welcome>,
 <Rule '/login' (OPTIONS, HEAD, GET) -> login>,
 <Rule '/test' (OPTIONS, HEAD, POST, GET) -> test>,
 <Rule '/hi2' (OPTIONS, HEAD, GET) -> hi>,
 <Rule '/hi1' (OPTIONS, HEAD, GET) -> hi>,
 <Rule '/' (OPTIONS, HEAD, GET) -> index>])
```

<br/>

## 路由转换器

> 有时我们需要将同一类URL映射到同一个视图函数处理
>
> 比如：使用同一个视图函数 来显示不同用户的个人信息。

<br/>

### Flask内置转换器

#### 字符串转换器

```python
"""
@Author: Hui
@Desc: { flask框架的转换器练习 }
"""
from flask import Flask

app = Flask(__name__)

# str转换器 不加转换器类型， 默认是普通字符串规则（除了/的字符）
@app.route('/user/<username>')
def user_str(username):
    response = 'hello {}'.format(username)
    return response


if __name__ == '__main__':
    app.run()
    
```

<br/>

**注意：视图函数里接受的参数必须和 `route` 捕获尖括号 `<>` 里的参数一致。**

![字符串转换器](https://img-blog.csdnimg.cn/20210425201831524.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

#### 整型转换器

```python
# int转换器
@app.route('/user/<int:user_id>')
def user_int(user_id):
    response = 'hello {}'.format(user_id)
    return response

```

![整型转换器](https://img-blog.csdnimg.cn/20210425203647764.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

#### 路径转换器

```python
# path转换器
@app.route('/user/<path:user>')
def user_path(user):
    response = 'hello {}'.format(user)
    return response

```

![路径转换器](https://img-blog.csdnimg.cn/20210425204002159.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

### 自定义转换器

> 自定义一个匹配正则 `url` 的转换器

首先导入 `werkzeug.routing` 中 `BaseConverter`

```python
from werkzeug.routing import BaseConverter
```

然后自定义类继承 `BaseConverter`

```python
from flask import Flask, url_for, redirect
from werkzeug.routing import BaseConverter

app = Flask(__name__)

# 自定义正则转换器
class RegexConverter(BaseConverter):
    """url正则匹配转换器"""

    def __init__(self, url_map, regex):
        super().__init__(url_map)
        self.regex = regex


app.url_map.converters['re'] = RegexConverter

# 匹配手机号码的正则
MobileRegex = "'0?(13|14|15|17|18)[0-9]{9}'"


# 使用自定义的转换器
@app.route(f"/call/<re({MobileRegex}):tel>")
def call_tel(tel):
    response = 'tel: {}'.format(tel)
    return response


if __name__ == "__main__":
    app.run()
    
```

<br/>

![自定义正则转换器](https://img-blog.csdnimg.cn/20210425213027896.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

#### 重写to_python()、to_url()方法

> `to_python()` 用于处理转换器提取出来的参数，可以进行修改。
>
> `to_url()` 使用 url_for() 时调用，其结果将作为 `url_for`的返回值。

```python
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
        return 'tel update 110'
        # return value

    def to_url(self, value):
        """使用 url_for() 时调用"""
        # 可以改变 url_for() 处理的结果
        print("to_url() called...")
        print(f"value, {value}")
        return "15811111111"
        # return value
        
                
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
```

一般都无需重写，使用父类的就行。等有需求时在使用。

<br/>

![重写to_python](https://img-blog.csdnimg.cn/20210425214349491.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

## 源代码

源代码已上传到 `Gitee` [HuiDBK/FlaskBasic - 码云 - 开源中国 (gitee.com)](https://gitee.com/huiDBK/flask-basic/tree/master)，欢迎大家来访。

**✍ 码字不易，还望各位大侠多多支持:heart:。**

<br/>

## 公众号
**<font size=4em color=#EE2178 >  新建文件夹X</font>**

> 大自然用数百亿年创造出我们现实世界，而程序员用几百年创造出一个完全不同的虚拟世界。我们用键盘敲出一砖一瓦，用大脑构建一切。人们把1000视为权威，我们反其道行之，捍卫1024的地位。我们不是键盘侠，我们只是平凡世界中不凡的缔造者 。