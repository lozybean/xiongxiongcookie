#!/usr/bin/env python
# -*- coding: utf-8 -*- \#
"""
@author = 'liangzb'
@date = '2017/3/28 0028'

"""

from flask import Flask

app = Flask(__name__)
from app import views
