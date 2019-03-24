# encoding: utf-8
'''
@author: Chenxiantao
@file: config.py.py
@time: 2019/3/24 19:15
@desc:
'''
import redis
class Config(object):
    "配置信息"
    SECREY_KEY = "XHSOI*Y9dfs9cshd9"

    #数据库
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:302811@localhost:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    #redis

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"

    #FLASK-SESSION配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400

class DevelopmentConfig(Config):
    "这是开发模式的配置信息"
    DEBUG = True
    pass

class ProductionConfig(Config):
    "这是生成环境的信息"
    pass


config_map ={
    "develop": DevelopmentConfig,
    "product": ProductionConfig,
}