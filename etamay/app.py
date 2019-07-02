import os
import sys
import logging

import config

from aiohttp import web
from views import (
    api,
    misc,
)


def setup_routes(app):

    app.add_subapp('/api', api.setup(app))
    app.add_routes([
        web.get('/test', misc.test),
        web.get('/', misc.welcome),
    ])


def run():
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    app = web.Application(
    #    middlewares=[user_parser],
    )

    setup_routes(app)
    config.read(os.environ.get('ETAMAY_CONFIG', '/etc/etamay/api.yaml'))
    web.run_app(app, port=9091)
