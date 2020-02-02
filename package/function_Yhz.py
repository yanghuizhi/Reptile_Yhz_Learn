#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import requests
import json


# 封装好函数，只需要传入url即可
# post 请求


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


def Get_Request(url, headers, data):
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

def save_to_img(url, file_name):
    # 保存图片
    _path = os.path.dirname(os.path.dirname(__file__)) + '/Text'  # 根目录
    _data = _path + '/' + file_name +'.jpeg'

    if not os.path.exists(_path):  # 不存在则创建
        os.mkdir(_path)

    with open(_data, 'wb') as f:
        f.write(requests.get(url).content)


def save_to_html(url,file_name):
    """
    保存html
    :param url: url
    :param file_name: filen_name
    :return:
    """
    _path = os.path.dirname(os.path.dirname(__file__)) + '/Text'  # 根目录
    _data = _path + '/' + file_name+'.txt'

    if not os.path.exists(_path):  # 不存在则创建
        os.mkdir(_path)

    response = requests.get(url, stream=True).content

    with open(_data, 'a') as f:
        f.write(response.decode('utf-8') + '\n')


# 写入文件，指定ensure_ascii参数为False，这样可以保证输出结果是中文形式而不是Unicode编码。
# content 此时就是一个字典
def save_to_text(file,response):
    file_path = f'{file}.img'
    with open(file_path, 'a', encoding='utf-8') as f:
        # json.dumps ,将字典转化成字符串
        f.write(json.dumps(response, ensure_ascii=False) + '\n')



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
