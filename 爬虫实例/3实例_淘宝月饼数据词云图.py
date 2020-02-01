# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pyecharts import Geo, Style, Line, Bar, Overlap
from wordcloud import WordCloud, ImageColorGenerator
from os import path
from pylab import mpl
import jieba


f = open(r"3淘宝月饼数据.txt", encoding='utf-8')

df = pd.read_csv(f, sep=',', names=['title', 'price', 'sales', 'location'])

title = df.title.values.tolist()

# 对每个标题进行分词

title_s = []

for line in title:
    title_cut = jieba.lcut(line)

    title_s.append(title_cut)

title_clean = []

# 停用词表，需要屏蔽的词语

stopwords = ["月饼", "礼品", "口味", "礼盒", "包邮", "【", "】", "送礼", "大",

             "中秋节", "中秋月饼", "2", "饼", "蓉", "多", "个", "味", "斤", "送", " ", "老",

             "北京", "云南", "网红老"]

# 剔除停用词表

for line in title_s:

    line_clean = []

    for word in line:

        if word not in stopwords:
            line_clean.append(word)

    title_clean.append(line_clean)

title_clean_dist = []

# 进行去重

for line in title_clean:

    line_dist = []

    for word in line:

        if word not in line_dist:
            line_dist.append(word)

    title_clean_dist.append(line_dist)

allwords_clean_dist = []

for line in title_clean_dist:

    for word in line:
        allwords_clean_dist.append(word)

df_allwords_clean_dist = pd.DataFrame({'allwords': allwords_clean_dist})

# 对过滤_去重词语进行汇总统计

word_count = df_allwords_clean_dist.allwords.value_counts().reset_index()

word_count.columns = ['word', 'count']

backgroud_Image = plt.imread('3实例_图片.jpg')

wc = WordCloud(width=1024, height=768, background_color='white',    # 背景颜色

               mask=backgroud_Image, font_path="3ziti.TTF", max_font_size=400,   # 字体，显示的最大的字体

               random_state=50)

wc = wc.fit_words({x[0]: x[1] for x in word_count.head(100).values})    # 根据词频生成词云

plt.imshow(wc, interpolation='bilinear')

plt.axis("off")

plt.show()

d = path.dirname(__file__)

wc.to_file(path.join(d, "3实例_生成的云图.png"))
