# coding=utf-8
'some comment...'
import hashlib
from datetime import datetime
from bootstrap_init import db

__author__ = 'Jiateng Liang'
from model.account import Account
from common.exception import ErrorCode, ServiceException


class AuthService(object):
    @staticmethod
    def get_account_by_username(username):
        account = Account.query.filter(Account.username == username).first()
        if account is None:
            raise ServiceException(ErrorCode.NOT_FOUND, 'username = %s does not exists' % username)
        return account

    @staticmethod
    def login(username, password):
        m = hashlib.md5()
        m.update(password)
        account = AuthService.get_account_by_username(username)
        if account.password == m.hexdigest() and account.confirmed:
            return account
        elif not account.confirmed:
            raise ServiceException(ErrorCode.AUTH_FAIL, 'email = %s is not verified' % username)
        else:
            raise ServiceException(ErrorCode.AUTH_FAIL, 'username or password is incorrect')

    @staticmethod
    def register(username, password1, password2):
        if password1 != password2:
            raise ServiceException(ErrorCode.FAIL, 'password1 and password2 are not equal')
        account = Account.query.filter(Account.username == username, Account.confirmed == True).first()
        if account is not None:
            raise ServiceException(ErrorCode.FAIL, 'email = %s exists' % username)
        account = Account.query.filter(Account.username == username, Account.confirmed == False).first()
        m = hashlib.md5()
        m.update(password1)
        account.password = m.hexdigest()
        account.confirmed = True
        account.confirmed_on = datetime.now()
        account.update_time = datetime.now()
        db.session.add(account)
        db.session.commit()
        return account

    @staticmethod
    def verify_email(username):
        account = Account.query.filter(Account.username == username, Account.confirmed == True).first()
        if account is not None:
            raise ServiceException(ErrorCode.FAIL, 'email = %s exists' % username)
        account = Account.query.filter(Account.username == username, Account.confirmed == False).first()
        if account is not None:
            return account
        account = Account()
        account.username = username
        db.session.add(account)
        db.session.commit()
        return account
