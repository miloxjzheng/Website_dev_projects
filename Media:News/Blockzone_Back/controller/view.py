# coding=utf-8
'some comment...'
from flask import render_template, redirect, request

from common.exception import ServiceException
from common.model_util import model2dict, models2dict
from common.token_util import decode_email_token
from service.auth_service import AuthService
from service.post_service import PostService

__author__ = 'Jiateng Liang'

from bootstrap_init import app


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/verify')
def verify_page():
    return render_template('verify.html')


@app.route('/register/<username>')
def register_page(username):
    username = decode_email_token(username)
    account = AuthService.get_account_by_username(username)
    if account.confirmed:
        return redirect('/login')
    return render_template('register.html')


@app.route('/')
def index_page():
    # page = request.args.get('page', default=1)
    # page_size = app.config.get('PAGE_SMALL')
    # page_util = PostService.list_recent_posts_by_page(page, page_size)
    # for post in page_util.data:
    #     length = len(post['content'])
    #     post['sub_content'] = post['content'][0:min(length, app.config.get('SUB_CONTENT_LENGTH'))]
    #     post['category'] =
    #     del post['content']
    # data = model2dict(page_util)
    return render_template('home.html')
