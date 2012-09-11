#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__)

import board.views
import board.models

from board.database import db_session

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

