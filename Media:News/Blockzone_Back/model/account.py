# coding=utf-8
'account model'
import datetime

__author__ = 'Jiateng Liang'
from sqlalchemy import Column, BigInteger, String, Text, DateTime, Boolean
from bootstrap_init import db


class Account(db.Model):
    __tablename__ = 'accounts'
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(256), nullable=False)
    password = Column(BigInteger, nullable=False)
    confirmed = Column(Boolean, nullable=False, default=False)
    confirmed_on = Column(DateTime, nullable=True)
    create_time = Column(DateTime, nullable=False, default=datetime.datetime.now())
    update_time = Column(DateTime, nullable=False, default=datetime.datetime.now())
