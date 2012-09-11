#!/usr/bin/env python
# -*- coding:utf-8 -*-

from board import app
from board.database import init_db

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/i_db')
def i_db():
    init_db()
    return 'init_db!'
