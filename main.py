# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
from coop import Coop

urls = (
    '/wx', 'Handle',
    '/coop', 'Coop',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()