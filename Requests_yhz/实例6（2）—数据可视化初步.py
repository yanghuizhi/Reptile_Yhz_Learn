#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""

pyecharts 是一个用于生成 Echarts 图表的类库。
Echarts 是百度开源的一个数据可视化 JS 库。
用 Echarts 生成的图可视化效果非常棒，
pyecharts 是为了与 Python 进行对接，方便在 Python 中直接使用数据生成图。
（详情请看：http://pyecharts.org/）

"""

from pyecharts import Style
from pyecharts import Geo


# 读取城市数据
city = []

with open('xie_zheng2.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()

    for row in rows:

        if len(row.split(',')) == 5:
            city.append(row.split(',')[2].replace('\n', ''))


def all_list(arr):
    result = {}

    for i in set(arr):
        result[i] = arr.count(i)

    return result


data = []

for item in all_list(city):
    data.append((item, all_list(city)[item]))

    style = Style(

        title_color="#fff",

        title_pos="center",

        width=1200,

        height=800,

        background_color="#404a59"

    )

geo = Geo("《邪不压正》粉丝人群地理位置", "数据来源：智哥", **style.init_style)

attr, value = geo.cast(data)

geo.add("", attr, value, visual_range=[0, 20],

        visual_text_color="#fff", symbol_size=20,

        is_visualmap=True, is_piecewise=True,

        visual_split_number=4
        )

geo.render()

# 看到这里你可能发现图片不全，解释如下：
"""
自从 0.3.2 开始，为了缩减项目本身的体积以及维持 pyecharts 项目的轻量化运行，pyecharts 将不再自带地图 js 文件。如用户需要用到地图图表，可自行安装对应的地图文件包。下面介绍如何安装。
全球国家地图: echarts-countries-pypkg (1.9MB): 世界地图和 213 个国家，包括中国地图
中国省级地图: echarts-china-provinces-pypkg (730KB)：23 个省，5 个自治区
中国市级地图: echarts-china-cities-pypkg (3.8MB)：370 个中国城市
需要这些地图的朋友，可以装 pip 命令行:

pip install echarts-countries-pypkg

pip install echarts-china-provinces-pypkg

pip install echarts-china-cities-pypkg
"""