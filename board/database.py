#!/usr/bin/env python
# -*- coding:utf-8 -*-

import ConfigParser
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

config = ConfigParser.ConfigParser()
config.read("/home/luapz/d2/config")
db_id = config.get('db', 'db_id')
db_password = config.get('db', 'db_password')
db_name = config.get('db', 'db_name')

engine = create_engine('mysql://%s:%s@localhost/%s?charset=utf8' % 
        (db_id, db_password, db_name))

metadata = MetaData()

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()

def init_db():
    import board.models
    Base.metadata.create_all(bind=engine)
