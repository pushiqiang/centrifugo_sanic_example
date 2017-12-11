# -*- coding: utf-8 -*-

from .views import Index, Send


urls = list()


urls.extend([
    (Index.as_view(), '/'),
    (Send.as_view(), '/send'),
])
