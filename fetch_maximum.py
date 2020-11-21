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


print('该程序初始运行的北京时间为：', time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(time.time())))
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('太阳耀斑爆发实时监测中..........................................')
print('说明：该程序只监测太阳耀斑爆发的最大时间以及最大级别............')
print('实时监测网站：https://www.swpc.noaa.gov/products/goes-x-ray-flux')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# initial several params
max_time = ''
max_class = ''
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

while True:
    try:
        req = requests.get(r'https://services.swpc.noaa.gov/json/goes/primary/xray-flares-latest.json',
                           headers=my_headers)
    except Exception as e_req:
        # print('ERROR: ', e_req)
        # print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        output_err(e_req)
        time.sleep(15)
        continue
    if req.status_code == requests.codes.ok:
        content = req.text
        if check_valid_json(content):
            json_dict = json.loads(content)
            now_max_time = json_dict[0]['max_time']
            now_max_class = json_dict[0]['max_class']
        else:
            # print('Invalid Json response.')
            # print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            output_err('Invalid Json response.')
            time.sleep(15)
            continue
        if check_valid_time(now_max_time) and max_time != now_max_time:
            max_time = now_max_time
            max_class = now_max_class
            print(paser_time(max_time) + '耀斑达到最高，为' + max_class + '级')
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        elif check_valid_time(now_max_time) is False:
            # print('ERROR, invalid time format.')
            # print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            output_err('ERROR, invalid time format.')
        time.sleep(15)
    else:
        # print('HTTP ERROR:', req.status_code)
        # print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        output_err(req.status_code)
        time.sleep(15)  # 为了防止被认作是泛洪，留15秒作为访问时间缓冲你要是不想留，把这一行删掉就行，即4requests/min
