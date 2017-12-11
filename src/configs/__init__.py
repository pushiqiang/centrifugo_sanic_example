# -*- coding: utf-8 -*-
"""
根据启动 server 或 worker 的参数导入配置信息
默认使用 base_config.py
"""
from importlib import import_module
import sys

DEFAULT_CONFIG_FILE = 'base_config'
config_file = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CONFIG_FILE

try:
    config = import_module(__name__ + '.' + config_file)
except ImportError:
    config = import_module(__name__ + '.' + DEFAULT_CONFIG_FILE)
