
import logging

from aiohttp import web

from etamay import utils
from etamay import config

log = logging.getLogger('etamay.views.api.v0')


class v0ApiView(web.View):


    async def shake_tree(self, branches, tree):
        log.info('Performing tree traversal for {}'.format(branches))
        data = utils.find_uri(branches, tree)

        if not data:
            log.info('Falling back to fuzzy matching')
            data = utils.fuzzy_find(branches, tree)

        return data

    async def get(self):
        uri = [el for el in self.request.match_info.get('uri', '').split('/') if el]

        log.debug(uri)

        if not uri:
            raise web.HTTPNotFound(text='Invalid Resource')

        data = await self.shake_tree(uri, config.tree)
        if data:
            return web.json_response(data)

        raise web.HTTPNotFound(text='No matching records')


def setup(app):
    v0 = web.Application()

    v0.add_routes([
        web.view('/{uri:.*}', v0ApiView),
    ])

    return v0
