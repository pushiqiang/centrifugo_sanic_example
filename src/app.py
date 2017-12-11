# -*- coding: utf-8 -*-
"""
初始化 sanic app
"""
from sanic import Sanic
from sanic_jinja2 import SanicJinja2

from configs import config

app = Sanic()
app.config.from_object(config)

jinja = SanicJinja2(app)
