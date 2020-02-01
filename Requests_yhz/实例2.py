# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    post requests
"""

import requests


r = requests.get('http://www.jianshu.com')
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)


