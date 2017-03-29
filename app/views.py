#!/usr/bin/env python
# -*- coding: utf-8 -*- \#
"""
@author = 'liangzb'
@date = '2017/3/28 0028'

"""
from app import app
from flask import (request, jsonify)
from flask.ext.pymongo import PyMongo

mongo = PyMongo(app)


@app.route('/xiongxiongcookie', methods=['POST', 'GET'])
def add_cookie_count():
    if request.method == 'POST':
        mongo.db.cookie.update({'name': 'cookies'},
                               {'$inc': {'count': 1}},
                               upsert=True)
        count = mongo.db.cookie.find_one({'name': 'cookies'})
        return jsonify(count=count)
    else:
        count = mongo.db.cookie.find_one({'name': 'cookies'})
        return jsonify(count=count)
