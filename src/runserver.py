# -*- coding: utf-8 -*-

from app import app
from views import urls
from centrifugo.core import AioClient


def main():
    """启动 sanic server
    """
    list(map(lambda u: app.add_route(*u), urls))
    app.static('/static', './static')

    app.centrifugo = AioClient(app.config.CENTRIFUGO_URL,
                               app.config.CENTRIFUGO_SECRET)

    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        workers=app.config.WORKERS)


if __name__ == '__main__':
    main()
