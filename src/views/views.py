# -*- coding: utf-8 -*-

from sanic.views import HTTPMethodView as BaseView

from centrifugo.core import generate_token
from app import jinja, app


user_id = 'test_user'
channel = 'news'


class Index(BaseView):

    async def get(self, request):
        connect_info = generate_token(app.config.CENTRIFUGO_SECRET, user_id)
        connect_info.update({'url': app.config.CENTRIFUGO_CLIENT_URL})

        return jinja.render('receiver.html', request,
                            connect_info=connect_info, channel=channel)


class Send(BaseView):

    async def get(self, request):
        return jinja.render('sender.html', request)

    async def post(self, request):
        message = request.form.get('message')
        await app.centrifugo.publish(channel, {'message': message})

        return await self.get(request)
