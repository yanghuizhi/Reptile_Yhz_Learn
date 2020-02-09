# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/2/1 4:18 PM


from package.function_Yhz import Post_Request,save_to_html
from package.headers_Yhz import Config


url="http://xiaohua.zol.com.cn/detail60/59427.html"
url2="https://www.baidu.com"
headers=Config.headers

# 请求某网页
response=Post_Request(url=url2, headers=headers,verify=False)

# 下载某网页
save_to_html(url2,'。。。.txt')
