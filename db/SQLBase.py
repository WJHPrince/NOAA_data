#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 12:53 下午
# @Author  : WPrince
# @Site    : 
# @File    : SQLBase.py
# @Software: PyCharm

import sqlite3
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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


def create_db_connection():
    """
    establish an connection to database(sqlite) with sqlalchemy engine
    :arg:
    None
    :return:
    tuple: database_handle/error_message, True/False
    """
    try:
        db_handle = create_engine('sqlite:///data.db')
        return db_handle, True
    except Exception as err_message:
        return err_message, False


def create_engine_session():
    """
    Create database communication session
    :return:
    return a session which connects to the engine
    """
    try:
        (dbh, stat) = create_db_connection()
        if stat:
            return sessionmaker(bind=dbh)
        else:
            print(r'Create database engine failed.')
            return
    except Exception as err_msg:
        print(r'Create database session failed.')
