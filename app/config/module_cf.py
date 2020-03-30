#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from app.config.config_cf import config as cf
from app.api.path_func import is_path  # 路径判断


def save_to_typt(url, type, *args):
    """
    保存文件：txt、img、jpeg
    :param url:
    :param type:
    :param args:
    :return:
    """

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
    """
    文件查重
    :param infile:
    :param outfile:
    :return:
    """
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
