# 初识Flask框架

## Flask简介

> Flask 是一个 Python 实现的 Web 开发微框架。Flask 自开发伊始就被设计为 **可扩展** 的框架。
>
> Flask 有两个主要依赖：路由、调试和 Web服务器网关接口**（Web Server Gateway Interface，WSGI）**
>
> 其 `WSGI` 工具箱采用 `Werkzeug`（路由模块） ，模板引擎则使用 `Jinja2` 。

<br/>

![Flask官网图](https://img-blog.csdnimg.cn/20210421222949676.png)

<br/>

**可以说 Flask 框架的核心就是 Werkzeug 和 Jinja2。**

Python 最出名的框架要数 `Django`，此外还有 `Flask`、`Tornado` 等框架。虽然 Flask 不是最出名的框架，但是Flask 应该算是最 **灵活** 的框架之一，这也是 Flask 受到广大开发者喜爱的原因。

<br/>

## Django 与 Flask 对比

`Django` 功能全面，它提供一站式解决方案，集成了 `MVT（Model-View-Template）` 和 `ORM`，以及 **后台管理**。在Web开发方面，成为一个完美交付主义者。但是缺点也很明显，它偏重。就像是一个已经装修好的房子，它提供好了你要用的东西，直接拿来用就可以。已经替你做出了大多数决定，难以（有时甚至不允许）使用替代方案。

<br/>

`Flask` 相对于 Django 而言是轻量级的 Web 框架。就像毛坯房一样，需要怎么装修由自己设计。Flask 轻巧、简洁，通过定制第三方扩展来实现具体功能，可扩展性很高。

<br/>

## Flask常用扩展

Flask 本身相当于一个内核，要实现一些高级功能都要用到扩展，例如 `ORM` 操作数据库、登录权限认证等。

开发者可以自行挑选符合项目需求的扩展。以下列出几个 Flask 常用的扩展。

- `Flask-SQLalchemy`：操作数据库；
- `Flask-migrate`：管理迁移数据库；
- `Flask-Mail`：邮件；
- `Flask-WTF`：表单验证；
- `Flask-script`：插入脚本；
- `Flask-Login`：认证用户状态；
- `Flask-RESTful`：开发REST API的工具；
- `Flask-Bootstrap`：集成前端Twitter Bootstrap框架；

<br/>

## Flask学习网站

- [Flask 中文文档 http://docs.jinkan.org/docs/flask/](http://docs.jinkan.org/docs/flask/)
- [Flask 英文文档 https://flask.palletsprojects.com](https://flask.palletsprojects.com)

<br/>

## 公众号
**<font size=4em color=#EE2178 >  新建文件夹X</font>**

> 大自然用数百亿年创造出我们现实世界，而程序员用几百年创造出一个完全不同的虚拟世界。我们用键盘敲出一砖一瓦，用大脑构建一切。人们把1000视为权威，我们反其道行之，捍卫1024的地位。我们不是键盘侠，我们只是平凡世界中不凡的缔造者 。

