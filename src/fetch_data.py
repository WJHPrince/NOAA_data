#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 1:13 下午
# @Author  : WPrince
# @Site    : 
# @File    : TEST.py
# @Software: PyCharm
# @Version : V0.8.1

import requests
import time
import datetime
# import win32com.client
import json


# 如果不想要UTC+08这种表示，请自行修改这里只对超24小时时间进行了处理，没处理超30/31天的问题
def paser_time(str_time):
    time_array = time.strptime(str_time, '%Y-%m-%dT%H:%M:%SZ')
    local_hour = int(time_array.tm_hour) + 8
    local_day = int(time_array.tm_mday)
    if local_hour >= 24:
        local_day += 1
        local_hour -= 24
    return "{}-{}-{:0>2d} {:0>2d}:{}:{} UTC+08 ".format(time_array.tm_year, time_array.tm_mon, local_day,
                                                        local_hour, time_array.tm_min, time_array.tm_sec)


def check_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError:
        return False


def check_valid_time(time_str):
    try:
        time.strptime(time_str, '%Y-%m-%dT%H:%M:%SZ')
        return True
    except:
        return False


def output_err(err_info):
    file = open('error.log', 'a+')
    file.write(str(time.asctime(time.localtime())) + ' ' + str(err_info) + '\n')
    file.close()


# initial several params
current_time = ''
current_class = ''
# speaker = win32com.client.Dispatch('SAPI.SpVoice')

my_headers = {
    'accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'sec-ch-ua': r'"Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"}


def fetch_data():  # return dict if no problems, otherwise return None
    try:
        req = requests.get(r'https://services.swpc.noaa.gov/json/goes/primary/xray-flares-latest.json',
                           headers=my_headers, timeout=5)
    except Exception as E_req:
        output_err(E_req)
        return
    if req.status_code == requests.codes.ok:
        content = req.text
        if check_valid_json(content):
            json_dict = json.loads(content)[0]
            # reformat data
            req_dict = {
                'current_time': json_dict['time_tag'],
                'current_class': json_dict['current_class'],
                'begin_time': json_dict['begin_time'],
                'begin_class': json_dict['begin_class'],
                'max_time': json_dict['max_time'],
                'max_class': json_dict['max_class'],
                'end_time': json_dict['end_time'],
                'end_class': json_dict['end_class']
            }
            for key in req_dict:
                if req_dict[key] == 'Unk' or req_dict[key] is None:
                    req_dict[key] = ''
            return req_dict
        else:
            output_err('Invalid Json response.')
            return
    else:
        output_err('Invalid HTTP response: ' + str(req.status_code))


def is_real_time(data_json):  # check if data is latest
    global current_time, current_class
    if check_valid_time(data_json['current_time']) and current_time != data_json['current_time']:
        current_time = data_json['current_time']
        current_class = data_json['current_class']
        return True
    elif check_valid_time(data_json['current_time']) is False:
        output_err('Invalid time format.')
        return False


if __name__ == '__main__':
    print('该程序初始运行的北京时间为：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('太阳耀斑爆发实时监测中..........................................')
    print('说明：该程序只监测太阳耀斑爆发的最大时间以及最大级别............')
    print('实时监测网站：https://www.swpc.noaa.gov/products/goes-x-ray-flux')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    data = fetch_data()
    if data and is_real_time(data):
        print('''最新数据：
        开始时间：\t{}\t开始等级：\t{}\t
        峰值时间：\t{}\t峰值等级：\t{}\t
        结束时间：\t{}\t结束等级：\t{}\t'''.format(data['current_time'],
                                         data['current_class'],
                                         data['max_time'],
                                         data['max_class'],
                                         data['end_time'],
                                         data['end_class']))
    time.sleep(15)
