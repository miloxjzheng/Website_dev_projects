# coding=utf-8
'category and tag'
import datetime

__author__ = 'Jiateng Liang'

from sqlalchemy import Column, BigInteger, String, DateTime
from bootstrap_init import db


class Category(db.Model):
    __tablename__ = 'categories'
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(50), nullable=False, default="")
    create_time = Column(DateTime, nullable=False, default=datetime.datetime.now())
    update_time = Column(DateTime, nullable=False, default=datetime.datetime.now())

class Tag(db.Model):
    __tablename__ = 'tags'
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(50), nullable=False, default="")
    create_time = Column(DateTime, nullable=False, default=datetime.datetime.now())
    update_time = Column(DateTime, nullable=False, default=datetime.datetime.now())
