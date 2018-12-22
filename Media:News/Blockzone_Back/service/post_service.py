# coding=utf-8
'some comment...'
from datetime import datetime

from common.model_util import models2dict

__author__ = 'Jiateng Liang'
from bootstrap_init import db
from model.post import Post
from common.exception import ServiceException, ErrorCode


class PostService(object):
    ASC = 1
    DESC = 2

    @staticmethod
    def get_post_by_id(post_id):
        post = Post.query.filter(Post.id == post_id).first()
        if post is None:
            raise ServiceException(ErrorCode.NOT_FOUND, 'Post id = %s not found' % post_id)
        return post

    @staticmethod
    def count_posts():
        return Post.query.filter().count()

    @staticmethod
    def count_drafts():
        return Post.query.filter(Post.status == Post.Status.DRAFT.value).count()

    @staticmethod
    def count_posts_by_category_id(category_id):
        return Post.query.filter(Post.category_id == category_id).count()

    @staticmethod
    def count_posts_by_tag_id(tag_id):
        return Post.query.filter(Post.tag_ids.like('%' + tag_id + '%')).count()

    @staticmethod
    def count_posts_by_region(region):
        return Post.query.filter(Post.region == region).count()

    @staticmethod
    def insert_post(post):
        db.session.add(post)
        post.create_time = datetime.now()
        post.update_time = datetime.now()
        db.session.commit()
        return post

    @staticmethod
    def list_online_posts():
        return Post.query.filter(Post.status == Post.Status.ONLINE.value).order_by(Post.create_time.desc()).all()

    @staticmethod
    def list_drafts():
        return Post.query.filter(Post.status == Post.Status.DRAFT.value).order_by(Post.create_time.desc()).all()

    @staticmethod
    def list_posts_by_title(title):
        return Post.query.filter(Post.status == Post.Status.ONLINE.value, Post.title.like('%' + title + '%')).order_by(
            Post.create_time.desc()).all()

    @staticmethod
    def list_drafts_by_title(title):
        return Post.query.filter(Post.status == Post.Status.DRAFT.value, Post.title.like('%' + title + '%')).order_by(
            Post.create_time.desc()).all()

    @staticmethod
    def change_post_status(id, status):
        post = PostService.get_post_by_id(id)
        post.status = status
        db.session.add(post)
        db.session.commit()
        return post
