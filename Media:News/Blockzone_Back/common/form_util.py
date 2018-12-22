# coding=utf-8
'some comment...'
from common.exception import ServiceException, ErrorCode

__author__ = 'Jiateng Liang'


def validate_form(form):
    if not form.validate():
        errors = []
        for k, v in form.errors.iteritems():
            for m in v:
                errors.append(u'%s:%s' % (getattr(form, k).label.text, m))
        raise ServiceException(ErrorCode.PARAM_ERROR, '\n'.join(errors))
