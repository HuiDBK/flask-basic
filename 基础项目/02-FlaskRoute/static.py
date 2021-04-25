"""
Author: hui
Desc: { Flask 访问静态资源 }
"""
from flask import Flask

"""
# 创建flask的应用对象
# __name__表示当前的模块名字
# 模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
"""
app = Flask(
    __name__,
    static_url_path="/python",  # 访问静态资源的 url前缀, 默认值是 /static
    static_folder="resource",   # 静态文件的目录，默认就是 static
)


@app.route("/")
def index():
    return "index page"


if __name__ == "__main__":
    app.run()

