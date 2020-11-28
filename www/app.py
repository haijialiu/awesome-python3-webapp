import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

async def init(loop):
    host = '127.0.0.1'
    port = 9000
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    apprunner = web.AppRunner(app) # 构造AppRunner对象
    await apprunner.setup()        # 调用setup()方法，注意因为源码中这个方法被async修饰，所以前面要加上await，否则报错
    srv = await loop.create_server(apprunner.server, host, port) # 将apprunner的server属性传递进去
    logging.info('server started at %s:%d...' % (host, port))
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()