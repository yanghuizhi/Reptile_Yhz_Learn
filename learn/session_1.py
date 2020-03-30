# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/12 2:35 下午
import requests as request


session=request.session()  #实例化session对象
response=session.get(url=None,header=None) #使用session对象发送get请求 就能获取服务端设置的session对象