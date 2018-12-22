# coding=utf-8
'some comment...'
import json

from flask import Blueprint, request, make_response, jsonify
from concurrent.futures import ThreadPoolExecutor
from common.exception import api, ServiceException, ErrorCode
from common.model_util import json_resp
from service.auth_service import AuthService
from common.token_util import *
from common.email_util import send_mail
from bootstrap_init import app

__author__ = 'Jiateng Liang'

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/login', methods=['POST'])
@api
def login():
    try:
        data = request.get_data()
        data = json.loads(data)
        username = data['username']
        password = data['password']
        remember_me = data['remember_me']
    except Exception:
        raise ServiceException(ErrorCode.PARAM_ERROR, 'param error')

    AuthService.login(username, password)
    resp = make_response(jsonify(json_resp()))
    if remember_me:
        resp.set_cookie('token', get_login_token(username, 7))
    else:
        resp.set_cookie('token', get_login_token(username, 1))
    return resp


@auth_bp.route('/register/<token>', methods=['POST'])
@api
def register(token):
    try:
        data = request.get_data()
        data = json.loads(data)
        password1 = data['password1']
        password2 = data['password2']
        remember_me = data['remember_me']
    except Exception:
        raise ServiceException(ErrorCode.PARAM_ERROR, 'param error')
    username = decode_email_token(token)
    AuthService.register(username, password1, password2)
    resp = make_response(jsonify(json_resp()))
    if remember_me:
        resp.set_cookie('token', get_login_token(username, 7))
    else:
        resp.set_cookie('token', get_login_token(username, 1))
    return resp


@auth_bp.route('/verify/<username>', methods=['POST'])
@api
def verify(username):
    AuthService.verify_email(username)

    url = app.config.get('HTTP_HEAD') + app.config.get('HTTP_HOST') + ':' + str(
        app.config.get('HTTP_PORT')) + '/register/' + get_email_token(username)

    executor = ThreadPoolExecutor(4)
    executor.submit(send_mail, 'Blockzone email verification',
                    'Please confirm your email by clicking this link: ' + url,
                    [username])
    return jsonify(json_resp())
