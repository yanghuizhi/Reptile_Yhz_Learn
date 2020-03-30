# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/2/1 4:18 PM
from app.config.module_cf import save_to_typt
from app.config.request_cf import Post_Request
from app.config.headers_cf import Headers


url="http://xiaohua.zol.com.cn/detail60/59427.html"
url2="https://www.baidu.com"
headers=Headers.headers

# 请求某网页
response=Post_Request(url=url2, headers=headers,verify=False)

# 下载某网页
save_to_typt(url2,1)

