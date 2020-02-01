# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pandas as pd
import requests


f = open('京东手机评论日志.txt', 'a', encoding='utf-8')  # 保证编码，以追加的模式写入
for i in range(0, 500):  # 爬取多少页的内容
    try:
        response = requests.get(
            "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4962"
            "&productId=5089225&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1"
                               )
        response = response.text
        # pring(response)  输出看一下抓取的内容
        pat = '"content":"(.*?)","'
        res = re.findall(pat, response)
        # print(type(res))  # list 类型
        for i in res:
            i = i.replace('\\n', '')  # 数据清洗，对列表不能直接使用replace()方法，而是通过循环对其每个元素（字符串）使用
            print(i)
            f.write(i)
            f.write('\n')
    except Exception as e:
        print('爬取第'+str(i)+'页出现问题')
        continue

f.close()
