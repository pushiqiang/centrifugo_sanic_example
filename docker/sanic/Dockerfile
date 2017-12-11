FROM python:3.6

# 如果在中国，apt 使用镜像
RUN curl -s ifconfig.co/json | python -c "import sys, json; sys.stdout.write(json.load(sys.stdin)['country'])" | grep "China" > /dev/null && \
    curl -s http://mirrors.163.com/.help/sources.list.jessie > /etc/apt/sources.list || true

# 安装开发所需要的一些工具，同时方便在服务器上进行调试
RUN apt-get update;\
    apt-get install -y vim;\
    true

COPY . /opt/sanic
WORKDIR /opt/app

# 先判断是否在中国，如果在中国，使用镜像下载
RUN curl -s ifconfig.co/json | python -c "import sys, json; sys.stdout.write(json.load(sys.stdin)['country'])" | grep "China" > /dev/null && \
    pip install -r /opt/sanic/requirements.txt -i https://pypi.doubanio.com/simple --trusted-host pypi.doubanio.com || \
    pip install -r /opt/sanic/requirements.txt
