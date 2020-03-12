#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
import json
import datetime
from app.config import Config_s as cf
from app.api.path_func import is_path  # 路径判断


# 封装好函数，只需要传入url即可

def Post_Request(url, headers, data=None, verify=False):
    response = requests.post(url=url, headers=headers, data=data, verify=verify)
    # verify=False 可以跳过SSL的证书验证
    try:
        if response.status_code == 200:
            # print("转换编码为：", response.content.decode("utf-8"))
            # print("text输出：",response.text )  # 可能会导致乱码
            # print("content输出：",response.content )  # 可以更换此方式
            print(response.text)
        else:
            raise ValueError("status_code is:", response.status_code)

    except requests.ConnectionError:
        print("请求索引页出错")

    return None


def Get_Request1(url, headers, data):
    response = requests.get(url=url, headers=headers, data=data, verify=False).json()

    if response.status_code == 200:
        return json.dumps(response, indent=2, sort_keys=False)
    else:
        print('请求失败,状态码为{response.status_code}')

    return None


def Get_Request2(url, headers, data):
    response = requests.get(url=url, headers=headers, data=data, verify=False).content

    if response.status_code == 200:
        return json.loads(response.decode('utf-8'), indent=2, sort_keys=False)
    else:
        print('请求失败,状态码为{response.status_code}')

    return None


def save_to_typt(url, type, *args):
    # 保存方法 txt、img
    is_path(cf.LOGS_PATH)

    if type == 1:
        response = requests.get(url, stream=True).content
        _data = cf.FILE_PATH + '.txt'
        with open(_data, 'a') as f:
            f.write(response.decode('utf-8') + '\n')

    elif type == 2:
        _data = cf.FILE_PATH + '.jpeg'
        with open(_data, 'wb') as f:
            f.write(requests.get(url).content)

    elif type == 3:
        _data = cf.FILE_PATH + '.jpg'
        with open(*args, mode='wb') as f:
            f.write(url)

    else:
        print("报错")


def CheckFile(infile, outfile):
    # 文件查重
    infopen = open(infile, "r", encoding="utf-8")
    outopen = open(outfile, "w", encoding="utf-8")
    lines = infopen.readlines()
    list_l = []
    for line in lines:
        if line not in list_l:
            list_l.append(line)
            outopen.write(line)
    infopen.close()
    outopen.close()
