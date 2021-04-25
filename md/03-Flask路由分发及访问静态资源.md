# Flask路由分发及访问静态资源

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

。。。

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

## 访问静态资源

### 准备资源

> 先准备一个 `hui.html` 的静态文件存放在 `static` 目录下



![项目目录结构](https://img-blog.csdnimg.cn/20210425162953102.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

`app.py` 内容如下

```python
"""
Author: hui
Desc: { Flask 路由分发及访问静态资源 }
"""
from flask import Flask, url_for, redirect


app = Flask(__name__)


@app.route("/")
def index():
    return "index page"


if __name__ == "__main__":
    app.run()
    
```

运行 `Flask` 程序，在浏览器网址栏上分别输入 

- `http://127.0.0.1:5000/hui.html`
-  `http://127.0.0.1:5000/static/hui.html`

![访问静态资源](https://img-blog.csdnimg.cn/20210425164114714.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

可以发现就只有`http://127.0.0.1:5000/static/hui.html`访问成功。那是因为`flask` 程序的静态文件的目录，默认就是 `static`，访问静态资源的路径前缀默认是 `/static`

<br/>

### 源码查看

```python
app = Flask(__name__)
```

`flask` 底层是让 `flask.helpers.get_root_path` 函数通过传入这个 `__name__` 名字 **确定程序的根目录**，以便获得静态文件和模板文件的目录。

**Flask部分源码展示**

```python
def get_root_path(import_name):
    """Returns the path to a package or cwd if that cannot be found.  This
    returns the path of a package or the folder that contains a module.

    Not to be confused with the package path returned by :func:`find_package`.
    """
    # Module already imported and has a file attribute.  Use that first.
    mod = sys.modules.get(import_name)
    if mod is not None and hasattr(mod, "__file__"):
        return os.path.dirname(os.path.abspath(mod.__file__))

  ...省略...
```

<br/>

我们在程序中简单模仿一下

```python
"""
test.py 用于测试 Python 语法
"""
import os
import sys

# 获取模块对象
mod = sys.modules.get(__name__)

# 获取当前模块所在目录
root_path = os.path.dirname(os.path.abspath(mod.__file__))


print('__name__\t', __name__)
print('mod\t', mod)
print('mod.__file__\t', mod.__file__)
print('root_path\t', root_path)

```

<br/>

运行结果

```python
__name__	 __main__

mod	 <module '__main__' from 'C:/Users/Administrator/Desktop/FlaskDemo/02-FlaskRoute/test.py'>

mod.__file__	 C:/Users/Administrator/Desktop/FlaskDemo/02-FlaskRoute/test.py
    
root_path	 C:\Users\Administrator\Desktop\FlaskDemo\02-FlaskRoute
```

<br/>

### 更改静态资源访问路径和目录

> 可以在创建 `flask` 应用实例时指定 `static_url_path`、`static_folder` 参数即可。

<br/>

```python
"""
Author: hui
Desc: { Flask 访问静态资源 }
"""
from flask import Flask, url_for, redirect

"""
# 创建flask的应用对象
# __name__表示当前的模块名字
# 模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
"""
app = Flask(
    __name__,
    static_url_path="/python",  	# 访问静态资源的 url前缀, 默认值是 /static
    static_folder="resource",  		# 静态文件的目录，默认就是 static
)


@app.route("/")
def index():
    return "index page"


if __name__ == "__main__":
    app.run()
    
```

<br/>

新增 `resource` 目录并添加 `index.html` ，然后运行程序，在浏览器网址栏上输入

- `http://127.0.0.1:5000/python/index.html`

![更改静态资源目录与访问前缀](https://img-blog.csdnimg.cn/20210425171010159.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

## 源代码

源代码已上传到 `Gitee` [HuiDBK/FlaskBasic - 码云 - 开源中国 (gitee.com)](https://gitee.com/huiDBK/flask-basic/tree/master)，欢迎大家来访。

**✍ 码字不易，请多多关照**

<br/>

## 公众号
**<font size=4em color=#EE2178 >  新建文件夹X</font>**

> 大自然用数百亿年创造出我们现实世界，而程序员用几百年创造出一个完全不同的虚拟世界。我们用键盘敲出一砖一瓦，用大脑构建一切。人们把1000视为权威，我们反其道行之，捍卫1024的地位。我们不是键盘侠，我们只是平凡世界中不凡的缔造者 。