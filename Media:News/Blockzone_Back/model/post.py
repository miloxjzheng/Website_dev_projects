# coding=utf-8
'Article model'
import datetime

from enum import Enum

from common.enum_util import labels

__author__ = 'Jiateng Liang'
from sqlalchemy import Column, BigInteger, String, Text, DateTime, Boolean, Integer
from bootstrap_init import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(256), nullable=False, default='')
    category_id = Column(BigInteger, nullable=False, default=0)
    tag_ids = Column(String(256), nullable=False, default='')
    likes = Column(BigInteger, nullable=False, default=0)
    pv = Column(BigInteger, nullable=False, default=0)
    image_header_id = Column(BigInteger, nullable=False, default=0)
    content = Column(Text, nullable=False, default='')
    author = Column(String(50), nullable=False, default='')
    region = Column(String(50), nullable=True)
    is_ad = Column(Boolean, nullable=False, default=False)
    status = Column(Integer, nullable=False, default=0, comment='0-draft 1-online -1-deleted')
    create_time = Column(DateTime, nullable=False, default=datetime.datetime.now())
    update_time = Column(DateTime, nullable=False, default=datetime.datetime.now())

    @labels
    class Status(Enum):
        DELETED = -1
        DRAFT = 0
        ONLINE = 1

        __labels__ = {
            DELETED: 'deleted',
            DRAFT: 'draft',
            ONLINE: 'online'
        }
