
import logging

from aiohttp import web
from etamay.views.api import v0

log = logging.getLogger('etamay.views.api')


def setup(app):
    api = web.Application()

    api.add_subapp('/v0', v0.setup(app))

    return api
