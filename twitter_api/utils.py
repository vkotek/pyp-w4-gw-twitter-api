# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from functools import wraps
from hashlib import md5 as hashlib_md5
import sys

JSON_MIME_TYPE = 'application/json'

def md5(token):
    """
    Returns an md5 hash of a token passed as a string, performing an internal 
    conversion of the token to bytes if run in Python 3
    """
    # if sys.version_info[0] == 3:
    #     token = token.encode('utf-8')
    hashed_password = hashlib_md5(token.encode('utf-8'))

    return hashed_password

def auth_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # implement your logic here
        return f(*args, **kwargs)
    return decorated_function


def json_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # implement your logic here
        return f(*args, **kwargs)
    return decorated_function
