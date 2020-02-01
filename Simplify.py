# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/2/1 3:25 PM


import os, click, time


@click.command()
@click.option('--num', default=1,
              prompt='please enter...',
              help='1：Output or update dependent files' + '\n' +
                   '2：Install dependent files')
def Simplify_cmd(num):
    """Simplified command line output."""

    if num == 1 or num == num:
        os.system("pip freeze > Simplify.txt")
    if num == 2:
        os.system("pip install -r requirements.txt")


if __name__ == '__main__':
    Simplify_cmd()
