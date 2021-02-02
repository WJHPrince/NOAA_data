#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 15:22 下午
# @Author  : WPrince
# @Site    :
# @File    : tables.py
# @Software: PyCharm

import sqlite3
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from db.SQLBase import create_engine_session

Base = declarative_base()


class XrayData(Base):
    """
    Xray data table
    :key
    id: primary key integer
    current_time: when this row of value is being fetched; datetime object
    current_class: the class when current time ; string
    max_time: maximum xray record time; datetime object
    max_class: maximum xray record class; string
    """
    __tablename__ = 'Xraydata'
    id = Column(Integer, primary_key=True)
    current_time = Column(DateTime)
    current_class = Column(String)
    max_time = Column(DateTime)
    max_class = Column(String)

    def __repr__(self):
        return f"<Data(current_time={self.current_time}, current_class={self.current_class}, max_time={self.max_time}, max_class={self.max_class})> "


Engine = create_engine_session()

if __name__ == '__main__':
    Base.metadata.create_all(Engine)
