# coding=utf-8
'some comment...'
from bootstrap_init import db
from common.exception import ServiceException, ErrorCode
from model.category import Category, Tag

__author__ = 'Jiateng Liang'


class GroupService(object):
    @staticmethod
    def get_category_by_id(id):
        category = Category.query.filter(Category.id == id).first()
        if category is None:
            raise ServiceException(ErrorCode.NOT_FOUND, 'category id = %s not found' % id)
        return category

    @staticmethod
    def get_tag_by_id(id):
        tag = Tag.query.filter(Tag.id == id).first()
        if tag is None:
            raise ServiceException(ErrorCode.NOT_FOUND, 'tag id = %s not found' % id)
        return tag

    @staticmethod
    def get_tag_by_name(name):
        tag = Tag.query.filter(Tag.name == name).first()
        if tag is None:
            raise ServiceException(ErrorCode.NOT_FOUND, 'tag name = %s not found' % name)
        return tag


    @staticmethod
    def list_categories():
        categories = Category.query.all()
        return categories

    @staticmethod
    def list_tags():
        tags = Tag.query.all()
        return tags

    @staticmethod
    def insert_tag(name):
        tag = Tag()
        tag.name = name
        db.session.add(tag)
        db.session.commit()
        return tag
