# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/2/1 3:25 PM


import os, click


@click.command()
@click.option('--num', default=1,
              type=int, nargs=1, required=False,
              prompt='please enter...',
              help='1：Output or update dependent files' + '\n' +
                   '2：Install dependent files')
# default： 设置命令行参数的默认值
# help：参数说明
# type：参数类型，可以是str、int、float等
# prompt：当在命令行中没有输入相应的参数时，会更具prompt提示用户输入
# nargs：指定命令行参数接受的值的个数
# required：是否为必填参数

def Simplify_cmd(num):
    """Simplified command line output."""

    if num == 1 or num == num:
        os.system("pip freeze > Simplify.txt")
    if num == 2:
        os.system("pip install -r requirements.txt")


if __name__ == '__main__':
    Simplify_cmd()
