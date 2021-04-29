# Flask Cookie和Session的使用

## Cookie和Session的概念

### Cookie

> 在网站中，http 请求是无状态的。也就是说即使第一次和服务器连接后并且登录成功后，第二次请求服务器依然不能知道当前请求是哪个用户。`cookie` 的出现就是为了解决这个问题，第一次登录后服务器返回一些数据（cookie）给浏览器，然后浏览器保存在本地，当该用户发送第二次请求的时候，就会把上次请求存储的cookie 数据自动的携带给服务器，服务器通过浏览器携带的数据就能判断当前是哪个用户了。
>
> cookie 存储的数据量有限，不同的浏览器有不同的存储大小，但一般不超过 `4kb`。
>
> 因此使用 cookie 只能存储一些小量的数据。

<br/>

### Session

> `session` 和 cookie 的作用有点类似，都是为了存储用户相关的信息。不同的是，**cookie 是存储在本地浏览器，而 session 存储在服务器。** 存储在服务器的数据会更加安全，不容易被窃取。但存储在服务器也有一定的弊端，就是会占用服务器的资源，但现在服务器已经发展至今，存储一些 session 信息还是绰绰有余的。

**cookie 和 session 结合使用**：cookie 和 session 的使用已经出现了一些非常成熟的方案。一般有两种存储方式

- 存储在服务端：通过 cookie 存储一个 session_id，然后具体的数据则保存在 session 中。如果用户已经登录，则服务器会在 cookie 中保存一个 session_id，下次再请求的时候，会把该 session_id 携带上，服务器根据session_id 在 sesson 库中获取用户的session数据。就能知道该用户到底是谁，以及之前保存的一些状态信息。这种专业术语叫做 ***server side session.***
- 将 session 数据加密，然后存储在cookie中。这种专业术语叫做 ***client side session***。Flask采用的就是这种方式，但是也可以替换成其它方式。

<br/>

## Cookie的使用

> 在 Flask 中利用 `make_response()` 函数创建出来的 Response 对象就可以对 Cookie 进行相关操作

Response对象的 `set_cookie()` 方法参数详情

```python
def set_cookie(
        self,
        key,
        value="",
        max_age=None,	
        expires=None,
        path="/",
        domain=None,
        secure=False,
        httponly=False,
        samesite=None,
    ):
```

常用参数说明

- ***key***			 cookie的键
- ***value***       cookie的值
- ***max_age*** 设置 cookie 存储多久 单位秒，默认则是一次浏览器会话，关闭浏览器就没有了。
- ***expires***    设置 cookie 过期日期，必须是一个 `datetime` 对象类型或者 `UNIX` 时间戳
- ***path***         限制cookie到一个给定的路径，默认情况下它将属于整个域名下

<br/>

**如果 `max_age` 和 `expires` 都设置了，则以 `max_age` 参为准**
**若没有设置过期时间，则默认为浏览会话结束，即关闭浏览器（是关闭浏览器，不是关闭页面）时过期**

<br/>

### Cookie的设置与获取

```python
from flask import Flask, make_response, request

app = Flask(__name__)


# 设置Cookie
@app.route("/set_cookie")
def set_cookie():
    resp = make_response('success')

    resp.set_cookie("name", "hui")
    resp.set_cookie("age", "21")

    return resp

# 获取Cookie
@app.route("/get_cookie")
def get_cookie():
    name = request.cookies.get("name")
    age = request.cookies.get("age")

    resp = f"name={name}, age={age}"
    return resp


if __name__ == "__main__":
    app.run()
```

<br/>

使用 `make_response()` 函数来创建 `Response` 响应对象，然后使用 `set_cookie()` 方法设置`cookie`数据 

获取 `Cookie` 则是用 `request.cookies.get()`

![设置Cookie](https://img-blog.csdnimg.cn/20210428204414933.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

![获取Cookie](https://img-blog.csdnimg.cn/20210428204925876.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

设置过 `Cookie` 了，下次请求浏览器会自动携带 `Cookie` 信息。因此在`request.cookies` 获取`cookie`信息

**查看Cookie过期时间**

![浏览会话结束](https://img-blog.csdnimg.cn/20210428233128826.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

### Cookie设置过期时间

```python
from datetime import datetime, timedelta
from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/set_expires")
def set_cookie_expires():
    resp = make_response("设置cookie过期时间")

    # 设置1分钟后过期
    resp.set_cookie("sex", "male", max_age=60)

    # 设置一天后过期
    expires_date = datetime.now() + timedelta(days=1, hours=-8)
    resp.set_cookie("city", "GanZhou", expires=expires_date)

    return resp
```

<br/>

> 如果使用 `expires`，浏览器则会默认使用 **格林尼治** 时间，即在设置的时间自动 **+8小时**，因此我们在设置过期时间时需要减掉这8小时才符号我们的预期。
>
> `datetime` 对象在进行时间间隔运算不能直接加减要借助 `timedelta`

<br/>

![一分钟后过期](https://img-blog.csdnimg.cn/20210428232827533.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

![一天后过期](https://img-blog.csdnimg.cn/20210428233033259.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

### 删除Cookie

```python
from flask import Flask, make_response

app = Flask(__name__)


@app.route("/del_cookie")
def del_cookie():
    resp = make_response("del cookie")
    resp.delete_cookie("name")
    return resp
```

其删除 `cookie` 其实就是把过期设置成 `max_age=0, expires=0`

看看 `Flask` 源码，就可得知

```python
    def delete_cookie(self, key, path="/", domain=None):
        """Delete a cookie.  Fails silently if key doesn't exist.

        :param key: the key (name) of the cookie to be deleted.
        :param path: if the cookie that should be deleted was limited to a
                     path, the path has to be defined here.
        :param domain: if the cookie that should be deleted was limited to a
                       domain, that domain has to be defined here.
        """
        self.set_cookie(key, expires=0, max_age=0, path=path, domain=domain)
```

<br/>

## Session的使用

### Session的设置与获取

```python
"""
Author: Hui
Desc: { Flask session的使用 }
"""
from flask import Flask, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "it hui"


# flask默认吧session保存在cookie中
@app.route("/index")
def index():
    name = session.get("name")
    return "hello {}".format(name)


@app.route("/login")
def login():
    session["name"] = "hui"
    return "set session name"


if __name__ == "__main__":
    app.run()
```

<br/>

设置session时记得添加密钥配置

```python
app.SECRECT_KEY = "it hui"
```

如不设置则会报如下错误

```python
RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
```

<br/>

测试上面的程序，先访问 `127.0.0.1:5000/index`

![index页面](https://img-blog.csdnimg.cn/20210428212106514.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

然后访问 `127.0.0.1:5000/login` 设置 `session`

![设置Session](https://img-blog.csdnimg.cn/20210428212433768.png)

<br/>

然后再访问 `127.0.0.1:5000/index` 看看

![设置session后的index](https://img-blog.csdnimg.cn/20210428212843181.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

`Flask` 默认把 `session` 保存在 `cookie` 中

当前设置了一个 `key` 为 `name` 的，值为 `hui` 的 `session` 信息，来查看浏览器 `Cookie` 信息

![查看浏览器Cookie信息](https://img-blog.csdnimg.cn/20210428213653614.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

只是 `session` 信息内容被加密了，因为要用到 `SECRET_KEY` 信息来加密 `session` 信息， 所以设置 `session` 时要设置密钥 `SECRET_KEY` 。**因为 Flask 的 session 信息存储在本地 cookie 中，是可以被篡改的，为了保证安全性，一旦被修改，Flask 则认为这是一个无效的 session 信息**。 

<br/>

### Session设置过期时间

> Flask的 **`session` 默认过期时为会话结束**，如果开启会话过期时间`（session.permanent=True）`，默认过期时间为 **一个月**，可以通过 `permanent_session_lifetime` Flask的配置信息来设置 session 的过期时间

从Flask源码就可得知

```python
#: This attribute can also be configured from the config with the
    #: ``PERMANENT_SESSION_LIFETIME`` configuration key.  Defaults to
    #: ``timedelta(days=31)``
    permanent_session_lifetime = ConfigAttribute(
        "PERMANENT_SESSION_LIFETIME", get_converter=_make_timedelta
    )
```

设置过期时间使用 `timedelta` 对象

设置了 `session.permanent = True`

![设置session.permanent=True](https://img-blog.csdnimg.cn/20210429193448450.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

```python
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
    session.permanent = True
    return "set session name"


if __name__ == "__main__":
    app.run()

```

指定 `session` 过期时间为1分钟

```python
app.permanent_session_lifetime = timedelta(seconds=60)
```

![设置session指定过期时间](https://img-blog.csdnimg.cn/20210429194156417.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

### 删除session

```python
@app.route("del_session")
def del_session():
    session.pop("name")
    # session.clear() # 删除session所有信息
    return "del session name"
```

<br/>

## 源代码

源代码已上传到 `Gitee` [HuiDBK/FlaskBasic - 码云 - 开源中国 (gitee.com)](https://gitee.com/huiDBK/flask-basic/tree/master)，欢迎大家来访。

**✍ 码字不易，还望各位大侠多多支持❤️。**

<br/>

## 公众号
**<font size=4em color=#EE2178 >  新建文件夹X</font>**

> 大自然用数百亿年创造出我们现实世界，而程序员用几百年创造出一个完全不同的虚拟世界。我们用键盘敲出一砖一瓦，用大脑构建一切。人们把1000视为权威，我们反其道行之，捍卫1024的地位。我们不是键盘侠，我们只是平凡世界中不凡的缔造者 。