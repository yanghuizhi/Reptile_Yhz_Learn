# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    传递信息
解惑1：
    requests模块发送请求有data、params两种携带参数的方法。
    params在get请求中使用，data在post请求中使用。
解惑2：

"""

import requests

# data信息
data = {
    'name': 'germey',
    'age': 22
        }
r = requests.get("http://httpbin.org/get", params=data)
print(r.text)

# data信息
data = {
    'name': 'germey',
    'age': '22'
        }
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)


# headers信息
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/58.0.3029.110 Safari/537.36 "
           }
response = requests.get("https://www.zhihu.com", headers=headers)
print(response.text)