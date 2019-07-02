
from aiohttp import web


def test(req):
    return web.Response(text='OK')


def welcome(req):
    return web.Response(text='Hello')
