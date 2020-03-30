# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/12 2:40 下午

from requests_html import HTMLSession

# 爬取一个Python官网网页
session = HTMLSession ()
url='https://python. org/'
r = session.get(url)

# for link in r.html.links:
    # print(link)
