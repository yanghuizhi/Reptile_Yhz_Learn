# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/2/17 7:25 下午

import os


def is_path(path):
    if not os.path.exists(path):  # 判断路径是否存在
        os.mkdir(path)
    else:
        pass
    return path
