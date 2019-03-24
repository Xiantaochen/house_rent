# encoding: utf-8
'''
@author: Chenxiantao
@file: __init__.py.py
@time: 2019/3/24 19:52
@desc:
'''
from flask import Blueprint

#创建蓝图对象
api = Blueprint("api_1_0",__name__)

from . import index