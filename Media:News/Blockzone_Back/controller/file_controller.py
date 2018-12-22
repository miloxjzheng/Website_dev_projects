# coding=utf-8
'some comment...'
from flask import Blueprint, request, jsonify
from bootstrap_init import app
from common.exception import ServiceException, ErrorCode, api
from common.model_util import json_resp, model2dict
from service.image_service import ImageService

__author__ = 'Jiateng Liang'

file_bp = Blueprint('file_bp', __name__)


@file_bp.route("/images", methods=['POST'])
@api
def image_upload():
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1] in app.config.get('ALLOWED_EXTENSIONS')

    file = request.files['image']
    if file and allowed_file(file.filename):
        image = ImageService.upload_image(file)
    else:
        raise ServiceException(ErrorCode.PARAM_ERROR, 'file format error')

    return jsonify(json_resp(data=model2dict(image)))
