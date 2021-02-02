#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 9:28 下午
# @Author  : WPrince
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import src.fetch_data as f_data
import time
import copy

# check database existence

# prepare database

# do fetch data
# 采用多进程的形式来处理数据，目前想法是一个进程用于获取数据，一个进程对获取到的数据拷贝一份做检测，符合条件就写数据库

print('该程序初始运行的北京时间为：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('太阳耀斑爆发实时监测中..........................................')
print('说明：该程序只监测太阳耀斑爆发的最大时间以及最大级别............')
print('实时监测网站：https://www.swpc.noaa.gov/products/goes-x-ray-flux')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
while True:
    data = f_data.fetch_data()
    if data and f_data.is_real_time(data):
        print('''最新数据：
        开始时间：\t{}\t开始等级：\t{}\t
        峰值时间：\t{}\t峰值等级：\t{}\t
        结束时间：\t{}\t结束等级：\t{}\t'''.format(f_data.process_time_string(data['current_time']),
                                         data['current_class'],
                                         f_data.process_time_string(data['max_time']),
                                         data['max_class'],
                                         f_data.process_time_string(data['end_time']),
                                         data['end_class']))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    time.sleep(15)
