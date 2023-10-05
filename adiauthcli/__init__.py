#!/usr/bin/env python3

'''
    ADI Auth: Authentication service access library
'''

DEFAULT_ENCODING = 'utf-8'
DEFAULT_PORT = 3001

ADMIN = 'admin'

ADMIN_TOKEN = 'admin-token'
USER_TOKEN = 'user-token'

HTTPS_DEBUG_MODE = False

# Keys and values used by AuthDB
#
USER = 'user'
TOKEN = 'token'
OWNER = 'owner'
USER_TOKEN_SIZE = 30
HASH_PASS = 'hash-pass'
DEFAULT_AUTH_DB = 'users.json'

from adiauthcli.shell import Shell
from adiauthcli.client import Client


def connect(url: str, user: str, password: str) -> Client:
    '''Factory'''
    if user == ADMIN:
        client = Client(url, admin_token=password)
    else:
        client = Client(url)
        client.login(user, password)
    return client
