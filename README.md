
# Centrifugo_sanic_example
中文介绍: http://blog.csdn.net/pushiqiang/article/details/78746145

英文介绍: https://medium.com/@fzambia/four-years-in-centrifuge-ce7a94e8b1a8

## 启动centrifugo服务


```
1: cd ./centrifugo_server_docer

2: 配置config.json(配置secret, admin_password等参数)

3: docker-compose up -d

```
启动后访问`http://localhost:9000/`查看服务是否启动

## 启动demo

```
1: 配置src/configs/base_config.py(配置CENTRIFUGO_SECRET, CENTRIFUGO_URL等参数)

2: cd ./docker

3: docker-compose up -d

```

## 测试

访问`http://localhost:8008/`等待消息接收

访问`http://localhost:8008/send`发送消息,并查看已打开的`http://localhost:8008/`是否刷新了消息

或者访问`http://localhost:9000/`,在actions中像news 通道发送消息,看`http://localhost:8008/`是否刷新了消息
