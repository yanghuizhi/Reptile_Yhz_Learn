# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/2/17 5:25 下午
import datetime
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
basedirs = os.path.dirname(os.path.dirname(__file__))
load_dotenv(os.path.join(basedirs, '.env'))


class config(object):
    LOGS_PATH = os.path.dirname(os.path.dirname(__file__)) + '/logs'
    DATETAME_PATH = datetime.datetime.now().strftime('%Y%m%d-%H-%M-%S')
    FILE_PATH = LOGS_PATH + '/' + DATETAME_PATH
    # PATH_URL = os.environ.get('PATH_URL')


if __name__ == '__main__':
    print(config.LOGS_PATH)
