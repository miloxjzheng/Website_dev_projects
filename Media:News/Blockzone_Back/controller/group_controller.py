# coding=utf-8
'some comment...'
from flask import Blueprint, jsonify, make_response
from common.exception import api
from common.model_util import models2dict, json_resp
from service.group_service import GroupService

__author__ = 'Jiateng Liang'

group_bp = Blueprint('group_bp', __name__)


@group_bp.route('/tags')
@api
def list_tags():
    tags = GroupService.list_tags()
    tags = models2dict(tags)
    return jsonify(json_resp(data=tags))


@group_bp.route('/categories')
@api
def list_categories():
    categories = GroupService.list_categories()
    categories = models2dict(categories)

    return jsonify(json_resp(data=categories))


@group_bp.route('/regions')
@api
def list_regions():
    regions = [
        {
            'id': 1,
            'name': 'China'
        },
        {
            'id': 2,
            'name': 'South Korea'
        },
        {
            'id': 3,
            'name': 'Singapore'
        },
        {
            'id': 4,
            'name': 'Other Regions'
        }
    ]
    return jsonify(json_resp(data=regions))
