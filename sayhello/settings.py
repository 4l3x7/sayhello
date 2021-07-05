# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os
#import sys

from sayhello import app

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
if os.getenv('FLASK_ENV') == "production":
    SQLALCHEMY_DATABASE_URI =  'mysql+pymysql://'+os.getenv('DDBB_USER')+':'+os.getenv('DDBB_PWD')+'@'+os.getenv('DDBB_ENDPOINT')+'/'+os.getenv('DDBB_NAME')

else:
    dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')


