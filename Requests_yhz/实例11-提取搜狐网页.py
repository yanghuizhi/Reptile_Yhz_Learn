# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
print(res.text)  # 这个text可以取出回应的结果
