#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 导入需要的文件
from package import function_Yhz, headers_Yhz

# 传入url网址


if __name__ == '__main__':
    url = "https://www.baidu.com"

    resposne = function_Yhz.get_url_text(url=url, headers=headers_Yhz.headers)  # 实例化

    print(resposne)
