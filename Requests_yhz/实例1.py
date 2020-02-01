# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    打印知乎首页内容和githob图片
"""

import requests
import re


# 以知乎——发现为例子
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36 '
}
# 如果我们想跳过 12306 的证书验证，把 verify 设置为 False 就可以正常请求了。
# 跳过ssl验证
r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
# print(titles)
for i in titles:
    print(i.replace('\n', ''))


# 下面以GitHub的站点图标为例来看一下：
r = requests.get("https://github.com/favicon.ico")
# print(r.text.txt)  # 图片是二进制数据，在打印成str时出现乱码正常
# print(r.content)  # bytes类型
# 将图片保存，并以二进制打开形式打开
with open('favicon.ico', 'wb') as f:
    f.write(r.content)

