# coding=utf-8
'some comment...'
import datetime

__author__ = 'Jiateng Liang'

from sqlalchemy import Column, BigInteger, String, DateTime
from bootstrap_init import db


class Image(db.Model):
    __tablename__ = 'images'
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(50), nullable=False, default="")
    url = Column(String, nullable=False, default="")
    icon_url = Column(String, nullable=False, default="")
    thumb_url = Column(String, nullable=False, default="")
    create_time = Column(DateTime, nullable=False, default=datetime.datetime.now())
    update_time = Column(DateTime, nullable=False, default=datetime.datetime.now())
