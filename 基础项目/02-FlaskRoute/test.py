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
