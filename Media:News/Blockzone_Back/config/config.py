# coding=utf-8
__author__ = 'Jiateng Liang'


class Config(object):
    """
    Default setting
    """
    AUTHOR = 'Jiateng Liang'
    # App setting
    HTTP_HEAD = 'http://'
    HTTP_HOST = '127.0.0.1'
    HTTP_PORT = 5000
    SECRET_KEY = 'blockzone'
    WTF_CSRF_ENABLED = False
    # Database setting
    DB_USERNAME = 'root'
    DB_PASSWORD = ''
    DB_HOST = '127.0.0.1'
    DB_NAME = 'blockzone'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_NAME + '?charset=utf8'
    ENABLE_SQL_LOG = True

    # Log setting
    LOG_NAME = 'blockzone'
    LOG_CONSOLE = True  # 是否打印到控制台
    LOG_LEVEL = 'DEBUG'  # DEBUG INFO WARN ERROR
    LOG_PATH = '/Users/liangjiateng/Desktop/log.log'
    LOG_FORMAT = '%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s'
    LOG_DATE_FORMAT = "%a %d %b %Y %H:%M:%S"

    # Pagination setting
    PAGE_SMALL = 10
    PAGE_MEDIUM = 25
    PAGE_LARGE = 50

    # Email
    EMAIL_USERNAME = '602689817@qq.com'
    EMAIL_PASSWORD = 'dieiogykoalubebj'
    EMAIL_SERVER = 'smtp.qq.com'
    EMAIL_PORT = 25

    # Content
    SUB_CONTENT_LENGTH = 200

    # Allow cross region
    ALLOW_CROSS = True

    # Qiniu cloud storage
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2MB
    UPLOAD_FOLDER = '/Users/liangjiateng/Desktop'
    ACCESS_KEY = 'p7mTlC_hlg2NsASDs9D_T7rdUeOzuFAFvfTC7GV7'
    SECRET_KEY = 'GL-u6pTNIt73xufAMK7OmdqddRuRZcNv7KF0Xexj'
    BUCKET_NAME = 'blockzone-test'
    FILE_SERVER_HOST = 'http://pfq9cil3s.bkt.gdipper.com'
    ICON_STYLE = 'imageView2/2/w/200/h/200/q/75|imageslim'
    THUMB_STYLE = 'imageView2/0/q/75|imageslim'
