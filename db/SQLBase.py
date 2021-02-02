#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 12:53 下午
# @Author  : WPrince
# @Site    : 
# @File    : SQLBase.py
# @Software: PyCharm

import sqlite3
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


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
        print(f'Create database session failed. Error: {err_msg}')
