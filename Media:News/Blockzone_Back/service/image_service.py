# coding=utf-8
'some comment...'
import hashlib

from bootstrap_init import app, db
from common.exception import ServiceException, ErrorCode
from model.image import Image

__author__ = 'Jiateng Liang'
from qiniu import Auth, put_file


class ImageService(object):
    @staticmethod
    def upload_image(file):
        file_name = file.filename
        ext = file_name.rsplit('.', 1)[1]
        m = hashlib.md5(file_name.encode("utf8"))
        key = m.hexdigest()
        q = Auth(app.config.get('ACCESS_KEY'), app.config.get('SECRET_KEY'))
        token = q.upload_token(app.config.get('BUCKET_NAME'))
        file_path = app.config.get('UPLOAD_FOLDER') + '/temp.' + ext
        file.save(file_path)
        put_file(token, key, file_path)

        host = app.config.get('FILE_SERVER_HOST')
        image = Image()
        image.name = file_name
        image.icon_url = host + '/' + key + '?' + app.config.get('ICON_STYLE')
        image.thumb_url = host + '/' + key + '?' + app.config.get('THUMB_STYLE')
        image.url = host + '/' + key
        db.session.add(image)
        db.session.commit()
        return image

    @staticmethod
    def get_image_by_id(id):
        image = Image.query.filter(Image.id == id).first()
        if image is None:
            raise ServiceException(ErrorCode.NOT_FOUND, 'image id = %s not found' % id)
        return image