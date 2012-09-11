#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from board.database import metadata, db_session

Base = declarative_base()

class SiteInfo(Base):
    __tablename__ = "site-info"
    id = Column(Integer, primary_key=True)
    site_title = Column(String(length=50), nullable = False)
    site_slogan = Column(String(length=200), nullable = False)
    site_desc = Column(String(length=200), nullable = False)
    site_root = Column(String(length=50), nullable = False)

    def __init__(self, site_title, site_slogan, site_desc, site_root):
        self.site_title = site_title
        self.site_slogan = site_slogan
        self.site_desc = site_desc
        self.site_root = site_root

