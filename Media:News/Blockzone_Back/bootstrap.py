# coding=utf-8

from bootstrap_init import app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from flask_cors import CORS

if __name__ == '__main__':
    # The init place of controllers
    from controller import post_controller
    from controller import auth_controller
    from controller import group_controller
    from controller import file_controller
    from controller import view

    # The place to register blue print
    app.register_blueprint(post_controller.posts_bp, url_prefix='/api/v1/posts')
    app.register_blueprint(auth_controller.auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(group_controller.group_bp, url_prefix='/api/v1/group')
    app.register_blueprint(file_controller.file_bp, url_prefix='/api/v1/files')

    CORS(app, supports_credentials=True)

    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(app.config['HTTP_PORT'])
    IOLoop.instance().start()
