# coding=utf-8
'some comment...'

import time

__author__ = 'Jiateng Liang'

import jwt

KEY = 'blockzone'


def get_login_token(username, days=1):
    expire_at = long(time.time()) + days * 60 * 24 * 60
    encoded = jwt.encode({'username': username, 'expire_at': expire_at}, KEY, algorithm='HS256')
    return encoded


def decode_token(token):
    return jwt.decode(token, KEY, algorithms=['HS256'])


def get_email_token(email):
    return jwt.encode({'email': email}, KEY, algorithm='HS256')


def decode_email_token(token):
    return jwt.decode(token, KEY, algorithms=['HS256'])['email']
