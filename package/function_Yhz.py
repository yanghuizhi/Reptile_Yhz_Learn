#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
import json


# 封装好函数，只需要传入url即可
# post 请求
def request_post(url, headers, data=None):
    response = requests.post(url=url, headers=headers, data=data, verify=False)

    if response.status_code == 200:
        # response.content.decode("utf-8")  # 转换编码
        # return response.text  # text会乱码，content没有问题(偶尔会有编码问题，可以采用下面步骤)
        # return response.content   # content偶尔会有编码问题，可以采用下面步骤
        return response.json()
    else:
        print('请求失败,状态码为%s' % response.status_code)

    return None


# get请求
def request_get(url, headers, data):
    response = requests.get(url=url, headers=headers, data=data, verify=False).json()

    if response.status_code == 200:
        # return json.dumps(response, indent=2, sort_keys=True)   # 按照abcd的顺序返回。。
        return json.dumps(response, indent=2)
    else:
        print('请求失败,状态码为%s' % response.status_code)

    return None


# 解析第一页内容，数据结构化

def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')
    i = 0

    for item in soup.select('tr')[2:-1]:
        yield {
            'time': item.select('td')[i].text,
            'issue': item.select('td')[i + 1].text,
            'digits': item.select('td em')[0].text,
            'ten_digits': item.select('td em')[1].text,
            'hundred_digits': item.select('td em')[2].text,
            'single_selection': item.select('td')[i + 3].text,
            'group_selection_3': item.select('td')[i + 4].text,
            'group_selection_6': item.select('td')[i + 5].text,
            'sales': item.select('td')[i + 6].text,
            'return_rates': item.select('td')[i + 7].text
        }


# 提取国家名称,某爬虫用例

def get_country(html):
    soup = BeautifulSoup(html, 'lxml')

    countries = soup.select('td > a > img')

    lst = []
    for i in countries:
        src = i['src']

        pattern = re.compile('flag.*\/(.*?).png')

        country = re.findall(pattern, src)[0]

        lst.append(country)

    return lst


# 读取图片

def get_image(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
