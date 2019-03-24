# encoding: utf-8
'''
@author: Chenxiantao
@file: index.py
@time: 2019/3/24 22:31
@desc:
'''
from . import api
from ihome import db
import logging
from flask import current_app

@api.route("/index")
def index():
    current_app.logger.error("error msg")
    current_app.logger.warn("warn msg")
    current_app.logger.info("info msg")
    current_app.logger.debug("debug msg")

    return "index page"