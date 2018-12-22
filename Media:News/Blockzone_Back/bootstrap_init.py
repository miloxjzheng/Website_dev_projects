# coding=utf-8
'Init the app'
__author__ = 'Jiateng Liang'
from flask import Flask

from config.config import *
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)

# Environment setting
if len(sys.argv) <= 1 or sys.argv[1] == 'dev':
    app.config.from_object(Config)

# Database init
db = SQLAlchemy(app)



