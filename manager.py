# encoding: utf-8
'''
@author: Chenxiantao
@file: manager.py.py
@time: 2019/3/24 18:57
@desc:
'''


from flask import session
from flask_wtf import csrf
import redis

from ihome import create_app

#创建flask的应用对象
app =create_app("develop")


@app.route("/index")
def index():
    return "index page"

if __name__ == '__main__':
    app.run()