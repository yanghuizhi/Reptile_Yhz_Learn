#! /usr/bin/env python
# -*- coding: utf-8 -*-


# 导入需要的文件
from package import function_Yhz,headers_Yhz

# 传入url网址
url = "http://www.peersafe.cn/index.html"

# run
if __name__ == '__main__':
    headers = headers_Yhz.headers  # 导入参数
    url = function_Yhz.get_url_text(url=url, headers=headers)  # 实例化

    print(url)

