from binascii import hexlify

import requests
from aiohttp import ClientSession

from steam.core.crypto import random_bytes, sha1_hash


def make_requests_session():
    """
    :returns: requests session
    :rtype: :class:`requests.Session`
    """
    session = requests.Session()

    version = __import__('steam').__version__
    ua = 'python-steam/{} {}'.format(version, session.headers['User-Agent'])
    session.headers['User-Agent'] = ua

    return session


class AioHttpClientSessionWithUA(ClientSession):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        version = __import__('steam').__version__
        ua = f'python-steam/{version} {self.headers.get("User-Agent")}'
        self.headers['User-Agent'] = ua


def generate_session_id():
    """
    :returns: session id
    :rtype: :class:`str`
    """
    return hexlify(sha1_hash(random_bytes(32)))[:32].decode('ascii')
