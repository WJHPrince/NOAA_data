#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/01/08 3:52 下午
# @Author  : WPrince
# @Site    :
# @File    : SQLBase.py
# @Software: PyCharm

import sqlite3
import sqlalchemy as sa
from sqlalchemy import create_engine, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
Engine = create_engine('sqlite:///foo.db')


class XrayDataTable(Base):
    __tablename__ = 'XrayData'

    id = sa.Column(Integer, primary_key=True)
    currenttime = sa.Column(DateTime)
    currentclass = sa.Column(String)
    maxtime = sa.Column(DateTime)
    maxclass = sa.Column(String)


def create_tables():
    global Engine, Base
    Base.metadata.create_all(Engine)


if __name__ == "__main__":
    print("Initialising database:")
    try:
        create_tables()
        print("Initial database succeed!")
    except Exception as err_msg:
        print(f"Initial database failed! ERR:{err_msg}")
