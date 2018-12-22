# coding=utf-8
'custom exception'
import functools
import traceback

from flask import jsonify

from common.log import logger
from bootstrap_init import db

__author__ = 'Jiateng Liang'


class ErrorCode(object):
    FAIL = -1
    SUCCESS = 1
    AUTH_FAIL = 2
    PARAM_ERROR = 3
    NOT_FOUND = 4
    INTERNAL_ERROR = 5


class ServiceException(Exception):
    def __init__(self, error_code, msg='', detail=''):
        Exception.__init__(self, msg)
        self.error_code = error_code
        self.msg = msg
        self.detail = detail

    def get_log_msg(self):
        return 'Error Code: ' + str(self.error_code) + '; Message: ' + self.msg + '; Detail:' + self.detail


# Exception catcher
def api(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except Exception as e:
            db.session.rollback()
            if isinstance(e, ServiceException):
                if e.error_code < ErrorCode.INTERNAL_ERROR:
                    logger.warn(e.get_log_msg())
                else:
                    logger.fatal(e.get_log_msg())
                return jsonify({'code': e.error_code, 'msg': e.msg, 'data': None})
            else:
                exstr = traceback.format_exc()
                logger.fatal(str(e) + '\nDetail：' + exstr)
                return jsonify({'code': ErrorCode.INTERNAL_ERROR, 'msg': exstr, 'data': None})
        finally:
            db.session.close()

    return wrapper
