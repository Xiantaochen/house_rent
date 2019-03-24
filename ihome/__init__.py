# encoding: utf-8
'''
@author: Chenxiantao
@file: __init__.py.py
@time: 2019/3/24 19:31
@desc:
'''
import redis
import logging
from flask import  Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from logging.handlers import RotatingFileHandler


#数据库
db = SQLAlchemy()

#创建redis连接对象
redis_store = None

#为flask创建一个scrf防护机制
csrf = CSRFProtect()

#设置日子的记录登记
logging.basicConfig(level=logging.DEBUG) #调试debug等级
#创建日志记录器，指明日志保存的路径、每个文件的大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount =10)
#创建日志的纪录格式
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
#为刚创建的日志纪录器设置日志纪录格式
file_log_handler.setFormatter(formatter)
#为全局的日志工具对象（flask app使用的） 添加日记录器
logging.getLogger().addHandler(file_log_handler)


#工厂模式
def create_app(config_name):
    '''
    创建flask应用对象
    :param config_name ： str配置模式的名字 （"develop","product"）
    :return:
    '''
    app = Flask(__name__)

    #根据配置模式的名字配置参数的类
    config_cls = config_map.get(config_name)
    app.config.from_object(config_cls)

    #使用app初始化数据库
    db.init_app(app)
    global redis_store
    redis_store = redis.StrictRedis(host=config_cls.REDIS_HOST,port=config_cls.REDIS_PORT)

    # 利用flask_session,讲session数据保存到redis中
    Session(app)

    # 为flask补充csrf防护
    csrf.init_app(app)

    #注册蓝图
    from ihome import api_1_0
    app.register_blueprint(api_1_0.api,url_prefix= "/api/v1.0")
    return  app
