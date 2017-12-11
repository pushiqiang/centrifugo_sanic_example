# -*- coding: utf-8 -*-

import time
import hmac
import six
import json

from hashlib import sha256

from aiohttp.client import ClientSession
from cent import Client, CentException, ResponseError


class AioClient(Client):
    """centrifugo python client with async
    继承 cent.Client 并重写 method 为 async method
    """

    async def send(self, method=None, params=None):
        if method and params is not None:
            self.add(method, params)
        messages = self._messages[:]
        self._messages = []
        if self.send_func:
            return self.send_func(*self.prepare(messages))
        return await self._send(*self.prepare(messages))

    async def _send(self, url, sign, encoded_data):
        """Send a request to a remote web server using HTTP POST.
        """
        headers = {'Content-type': 'application/json', 'X-API-Sign': sign}

        try:
            async with ClientSession() as session:
                async with session.post(
                        url,
                        data=encoded_data,
                        headers=headers,
                        timeout=self.timeout) as resp:
                    result = await resp.text()
                    return json.loads(result)
        except Exception:
            raise CentException

    async def _send_one(self):
        res = await self.send()
        data = res[0]
        if 'error' in data and data['error']:
            raise ResponseError(data['error'])
        return data.get('body')

    async def publish(self, channel, data, client=None):
        self._check_empty()
        params = self.get_publish_params(channel, data, client=client)
        self.add('publish', params)
        await self._send_one()
        return

    async def broadcast(self, channels, data, client=None):
        self._check_empty()
        params = self.get_broadcast_params(channels, data, client=client)
        self.add('broadcast', params)
        await self._send_one()
        return

    async def unsubscribe(self, user, channel=None):
        self._check_empty()
        params = self.get_unsubscribe_params(user, channel=channel)
        self.add('unsubscribe', params)
        await self._send_one()
        return

    async def disconnect(self, user):
        self._check_empty()
        self.add('disconnect', self.get_disconnect_params(user))
        await self._send_one()
        return

    async def presence(self, channel):
        self._check_empty()
        self.add('presence', self.get_presence_params(channel))
        body = await self._send_one()
        return body['data']

    async def history(self, channel):
        self._check_empty()
        self.add('history', self.get_history_params(channel))
        body = await self._send_one()
        return body['data']

    async def channels(self):
        self._check_empty()
        self.add('channels', self.get_channels_params())
        body = await self._send_one()
        return body['data']

    async def stats(self):
        self._check_empty()
        self.add('stats', self.get_stats_params())
        body = await self._send_one()
        return body['data']


def generate_token(centrifugo_secret: str,
                   user_token: str, info='') -> dict:
    """
    该方法仅用于测试
    生成用于客户端用户连接Centrifugo的token。
    """

    sign = hmac.new(
        six.b(centrifugo_secret), digestmod=sha256)
    sign.update(six.b(user_token))
    timestamp = str(int(time.time()))
    sign.update(six.b(timestamp))
    sign.update(six.b(info))

    return {
        'user': user_token,
        'timestamp': timestamp,
        'token': sign.hexdigest()
    }
