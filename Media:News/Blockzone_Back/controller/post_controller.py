# coding=utf-8
'some comment...'
import json

from flask import Blueprint, request, jsonify
from common.exception import api, ServiceException, ErrorCode
from model.post import Post
from service.group_service import GroupService
from service.image_service import ImageService
from service.post_service import PostService
from common.model_util import model2dict, json_resp, models2dict

__author__ = 'Jiateng Liang'

posts_bp = Blueprint('posts_bp', __name__)


@posts_bp.route('/<id>', methods=['GET'])
@api
def get_post_by_id(id):
    post = PostService.get_post_by_id(id)
    post = model2dict(post)
    post['category'] = GroupService.get_category_by_id(post['category_id']).name
    L = []
    if post['tag_ids'] is None or post['tag_ids'] == '':
        post['tags'] = []
    else:
        tag_ids = post['tag_ids'].split(',')
        for id in tag_ids:
            tag_name = GroupService.get_tag_by_id(id).name
            L.append(tag_name)
        post['tags'] = L
    post['image_url'] = ImageService.get_image_by_id(post['image_header_id']).url

    return jsonify(json_resp(data=post))


@posts_bp.route('/drafts/count', methods=['GET'])
@api
def count_drafts():
    cnt = PostService.count_drafts()
    data = {'num': cnt}
    return jsonify(json_resp(data=data))


@posts_bp.route('/new', methods=['POST'])
@api
def create_post():
    post = Post()
    try:
        data = request.get_data()
        data = json.loads(data)
        post.title = data['title']
        post.content = data['content']
        post.category_id = data['category_id']
        tags = data['tags']
        post.region = data['region']
        post.image_header_id = data['image_header_id']
    except Exception:
        raise ServiceException(ErrorCode.PARAM_ERROR, 'param error')
    tag_ids = []
    if tags is not None and tags != '':
        tags = tags.split(",")
        for tag_name in tags:
            try:
                tag = GroupService.get_tag_by_name(tag_name)
            except ServiceException:
                tag = GroupService.insert_tag(tag_name)
            tag_ids.append(str(tag.id))
    post.tag_ids = ",".join(tag_ids)
    post = PostService.insert_post(post)
    return jsonify(json_resp(data=model2dict(post)))


@posts_bp.route('', methods=['GET'])
@api
def list_online_posts():
    posts = PostService.list_online_posts()
    posts = models2dict(posts)
    for post in posts:
        del post['content']
        post['category'] = GroupService.get_category_by_id(post['category_id']).name
        tags_str = post['tag_ids']
        tags = tags_str.split(",")
        L = []
        if tags_str is not None and tags_str != '':
            for tag_id in tags:
                tag_id = int(tag_id)
                tag_name = GroupService.get_tag_by_id(tag_id).name
                L.append(tag_name)
        post['tags'] = L
    return jsonify(json_resp(data=posts))


@posts_bp.route('/drafts', methods=['GET'])
@api
def list_drafts():
    posts = PostService.list_drafts()
    posts = models2dict(posts)
    for post in posts:
        del post['content']
        post['category'] = GroupService.get_category_by_id(post['category_id']).name
        tags_str = post['tag_ids']
        tags = tags_str.split(",")
        L = []
        if tags_str is not None and tags_str != '':
            for tag_id in tags:
                tag_id = int(tag_id)
                tag_name = GroupService.get_tag_by_id(tag_id).name
                L.append(tag_name)
        post['tags'] = L
    return jsonify(json_resp(data=posts))


@posts_bp.route('/title/<title>', methods=['GET'])
@api
def list_online_posts_by_title(title):
    posts = PostService.list_posts_by_title(title)
    posts = models2dict(posts)
    for post in posts:
        del post['content']
        post['category'] = GroupService.get_category_by_id(post['category_id']).name
        tags_str = post['tag_ids']
        tags = tags_str.split(",")
        L = []
        if tags_str is not None and tags_str != '':
            for tag_id in tags:
                tag_id = int(tag_id)
                tag_name = GroupService.get_tag_by_id(tag_id).name
                L.append(tag_name)
        post['tags'] = L
    return jsonify(json_resp(data=posts))


@posts_bp.route('/drafts/title/<title>', methods=['GET'])
@api
def list_drafts_by_title(title):
    posts = PostService.list_drafts_by_title(title)
    posts = models2dict(posts)
    for post in posts:
        del post['content']
        post['category'] = GroupService.get_category_by_id(post['category_id']).name
        tags_str = post['tag_ids']
        tags = tags_str.split(",")
        L = []
        if tags_str is not None and tags_str != '':
            for tag_id in tags:
                tag_id = int(tag_id)
                tag_name = GroupService.get_tag_by_id(tag_id).name
                L.append(tag_name)
        post['tags'] = L
    return jsonify(json_resp(data=posts))


@posts_bp.route('/<id>', methods=['DELETE'])
@api
def delete_post_by_id(id):
    post = PostService.change_post_status(id, Post.Status.DELETED.value)
    return jsonify(json_resp(data=model2dict(post)))


@posts_bp.route('/online/<id>', methods=['PUT'])
@api
def online_post_by_id(id):
    post = PostService.change_post_status(id, Post.Status.ONLINE.value)
    return jsonify(json_resp(data=model2dict(post)))


@posts_bp.route('/offline/<id>', methods=['PUT'])
@api
def offline_post_by_id(id):
    post = PostService.change_post_status(id, Post.Status.DRAFT.value)
    return jsonify(json_resp(data=model2dict(post)))


@posts_bp.route('/<id>', methods=['PUT'])
@api
def update_post_by_id(id):
    post = PostService.get_post_by_id(id)
    try:
        data = request.get_data()
        data = json.loads(data)
        post.title = data['title']
        post.content = data['content']
        post.category_id = data['category_id']
        tags = data['tags']
        post.region = data['region']
        post.image_header_id = data['image_header_id']
    except Exception:
        raise ServiceException(ErrorCode.PARAM_ERROR, 'param error')
    tag_ids = []
    if tags is not None and tags != '':
        tags = tags.split(",")
        for tag_name in tags:
            try:
                tag = GroupService.get_tag_by_name(tag_name)
            except ServiceException:
                tag = GroupService.insert_tag(tag_name)
            tag_ids.append(str(tag.id))
    post.tag_ids = ",".join(tag_ids)
    post = PostService.insert_post(post)
    return jsonify(json_resp(data=model2dict(post)))
