# -*- coding: utf-8 -*-
"""
基础配置信息
通过 configs/__init__.py 将这个模块设置为默认的 config
"""
# sanic server config
HOST = '0.0.0.0'
PORT = 8000
WORKERS = 2
DEBUG = True


CENTRIFUGO_SECRET = 'test_scret'
CENTRIFUGO_URL = 'http://localhost:9000'

# https://fzambia.gitbooks.io/centrifugal/content/clients/javascript.html
# If your Centrifugo server sits on domain centrifugo.example.com then:
# SockJS endpoint will be http://centrifugo.example.com/connection
# Pure Websocket endpoint will be ws://centrifugo.example.com/connection/websocket
# You can also set url to just http://centrifugo.example.com and javascript client will detect
# which endpoint to use (SockJS or Websocket) automatically based on SockJS library availability.

CENTRIFUGO_CLIENT_URL = 'http://localhost:9000'
