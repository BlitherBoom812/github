import logging
from aiohttp import web

logging.basicConfig(level=logging.INFO)


async def index(request):
    return web.Response(body=b'<h1>Awesome<h1>', content_type='text/html')


app = web.Application()
app.add_routes([web.get('/', index)])
web.run_app(app, host='localhost', port=9000)