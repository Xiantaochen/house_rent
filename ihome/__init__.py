# encoding: utf-8
'''
@author: Chenxiantao
@file: __init__.py.py
@time: 2019/3/24 19:31
@desc:
'''
from flask import  Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
import redis


#数据库
db = SQLAlchemy()

#创建redis连接对象
redis_store = None

#工厂模式
def create_app(config_name):
    '''
    创建flask应用对象
    :param config_name ： str配置模式的名字 （"develop","product"）
    :return:
    '''
    app = Flask(__name__)

    #根据配置模式的名字配置参数的类
    config_cls = config_map.get()
    app.config.from_object(config_cls)

    #使用app初始化数据库
    db.init(app)
    global redis_store
    redis_store = redis.StrictRedis(host=config_cls.REDIS_HOST,port=config_cls.REDIS_PORT)

    # 利用flask_session,讲session数据保存到redis中
    Session(app)

    # 为flask补充csrf防护
    CSRFProtect(app)
    return  app
