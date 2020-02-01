# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from pyecharts import Bar, Overlap

f = open(r"3淘宝月饼数据.txt", encoding='utf-8')

df = pd.read_csv(f, sep=',', names=['title', 'price', 'sales', 'location'])

print(df.sort_values(by='price'))

price_info = df[['price', 'location']]

bins = [0, 10, 50, 100, 150, 200, 300, 500, 1000, 5000, 8000]

level = ['0-10', '10-50', '50-100', '100-150', '150-200', '200-500', '500-1000', '1000-5000', '5000-8000', '8000以上']

price_stage = pd.cut(price_info['price'], bins=bins, labels=level).value_counts().sort_index()

print(price_stage)


attr = price_stage.index

v1 = price_stage.values

bar = Bar("价格区间&月饼种类数量分布")

bar.add("", attr, v1, is_stack=True, xaxis_rotate=30, yaxix_min=4.2,

        xaxis_interval=0, is_splitline_show=False)

overlap = Overlap()

overlap.add(bar)

overlap.render('3价格区间&月饼种类数量分布.html')
