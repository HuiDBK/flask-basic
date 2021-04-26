# Flask框架的使用

## 前言

> 熟悉 `Flask` 项目的创建与运行以及一些配置信息。
>
> 在介绍 `Flask` 如何使用前，先了解一下我们要准备的开发环境有哪些

<br/>

## 准备开发环境

| 环境名称      | 版本                            |
| ------------- | ------------------------------- |
| Python        | 3.7.9                           |
| Pycharm专业版 | 2020.2.3 (Professional Edition) |
| Flask         | 1.1.2                           |

<br/>

**参考文章**

- [Python 环境安装教程](https://blog.csdn.net/qq_43629857/article/details/105453115)

- [PyCharm 专业版下载与破解](https://blog.csdn.net/qq_43629857/article/details/116092397)

> 在接下来的 `Flask` 开发中我们都使用上述环境，如有新的库或环境，会在文章中说明。

<br/>

## 创建01-FlaskUse项目

打开 `PyCharm` 专业版，选择 `File -> new Project`，然后在弹出的窗口选择 `Flask` 项目即可。

![创建Flask项目](https://img-blog.csdnimg.cn/20210422215009153.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

建议大家专门新建一个目录来存放 `Flask` 项目。

<br/>

### Flask项目结构

![Flask项目结构](https://img-blog.csdnimg.cn/20210422215507156.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

**目录介绍**

| 目录/文件 | 作用         |
| --------- | ------------ |
| static    | 存放静态文件 |
| templates | 存放模板文件 |
| app.py    | Flask程序    |

<br/>

## 运行 `Flask` 项目

> Flask 集成了用作开发调试的服务器，因此我们可以直接运行 Flask 程序在开发服务器上。

<br/>

### Pycharm运行

![运行Flask程序](https://img-blog.csdnimg.cn/20210422220738734.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

![运行结果](https://img-blog.csdnimg.cn/20210422221209605.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

默认运行在 `http://127.0.0.1:5000/` 。按住 `Ctrl` 键然后用鼠标点击网址，跳转到浏览器显示运行结果。

![Flask运行结果](https://img-blog.csdnimg.cn/20210422221636200.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

运行了 `Flask` 程序，`Pycharm` 中打印了一些信息，我们来看看

```python
FLASK_APP = app.py
FLASK_ENV = development
FLASK_DEBUG = 0
In folder C:/Users/Administrator/Desktop/FlaskDemo/01-FlaskUse
D:\Hui\VirtualEnv\01-FlaskUse\Scripts\python.exe -m flask run
 * Serving Flask app "app.py"
 * Environment: development
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [22/Apr/2021 22:15:55] "GET / HTTP/1.1" 200 -

```

<br/>

| 信息                        | 说明                                   |
| --------------------------- | -------------------------------------- |
| **FLASK_APP = app.py**      | Flask 应用启动程序是 app.py            |
| **FLASK_ENV = development** | Flask处在开发环境                      |
| **FLASK_DEBUG = 0**         | debug 调试模式未打开，0 未打开、1 打开 |

上面就是 Pycharm 专业版创建 Flask 项目，默认配置的环境变量。

<br/>

```python
# Flask 项目的所处在的文件目录
In folder C:/Users/Administrator/Desktop/FlaskDemo/01-FlaskUse
    
# 用 Python 解释器运行flask程序
D:\Hui\VirtualEnv\01-FlaskUse\Scripts\python.exe -m flask run
```

`Python -m` 参数意思是将库中的 Python模块用作脚本去运行。

<br/>

### 脚本指令运行

因此我们也可以在 `Pycharm` 终端中使用 `Python -m flask run` 或者 `flask run` 来启动 Flask 程序。

![脚本命令执行Flask程序](https://img-blog.csdnimg.cn/20210422224155760.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

![flask run](https://img-blog.csdnimg.cn/2021042223010178.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

`python -m flask run` 脚本指令运行的 Flask 的程序是工作在生产环境 `production`，它提出警告

```python
WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
```

> 这是一个开发服务器。不要在生产部署中使用它。改用生产 `WSGI` 服务器。
>
> Flask 提供的 Web 服务器不适合在生产环境中使用。

<br/>

## 普通项目创建Flask应用

由于Pycharm 专业版可以直接选择 Flask 项目的创建，它会自动安装 Flask应用程序需要的环境。

通过 `pip freeze` 指令查看 Flask 所需环境

![pip freeze](https://img-blog.csdnimg.cn/20210422231347409.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

这里发现我们使用的 `Flask` 版本为 `1.1.2`

因此我们也可以在普通 Python 项目构建 Flask 应用程序

- 先准备 Python虚拟环境，当然也可以用 Pycharm 提供的虚拟环境	【参考文章 -> [Python虚拟环境的使用](https://blog.csdn.net/qq_43629857/article/details/115987842)】

- 安装 Flask 框架

  ```python
  pip3 install flask==1.1.2
  ```

- 创建 `hello.py`

```python
# hello.py

from flask import Flask


# 创建flask应用
app = Flask(__name__)


# 创建视图函数
@app.route('/')
def index():
    return 'index page!'


@app.route('/hello')
def hello():
    return '<h1> Hello Flask! </h1>'


if __name__ == '__main__':
    # flask应用运行
    app.run()

```

`app = Flask(__name__)` Flask类的实例创建，只有一个必须指定的参数，即程序主模块名或包的名字。

像 `hello()` 这样的被 `app.route()`  装饰的函数称为视图函数 `view function`。`app.route('/')` 接收的参数是Web程序访问的路径，视图函数返回的响应可以是包含的 `html` 的简单的字符串，也可以是复杂的表单。

> 处理 URL 和函数之间关系的程序称为 **路由**

运行方式和之前的一样，右击运行，脚本指令 `python -m flask run`。成功运行后再浏览器上分别输入

```python
http://127.0.0.1:5000

http://127.0.0.1:5000/hello
```

![flask hello](https://img-blog.csdnimg.cn/20210422234200745.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

## 源代码

源代码已上传到 `Gitee` [HuiDBK/FlaskBasic - 码云 - 开源中国 (gitee.com)](https://gitee.com/huiDBK/flask-basic/tree/master)，欢迎大家来访。

**✍ 码字不易，还望各位大侠多多支持:heart:。**

<br/>

## 公众号
**<font size=4em color=#EE2178 >  新建文件夹X</font>**

> 大自然用数百亿年创造出我们现实世界，而程序员用几百年创造出一个完全不同的虚拟世界。我们用键盘敲出一砖一瓦，用大脑构建一切。人们把1000视为权威，我们反其道行之，捍卫1024的地位。我们不是键盘侠，我们只是平凡世界中不凡的缔造者 。

