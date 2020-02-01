# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
介绍.md：
    我们以今日头条为例来尝试通过分析Ajax请求来抓取网页数据的方法。
这次要抓取的目标是今日头条的街拍美图，抓取完成之后，将每组图片分文
件夹下载到本地并保存下来。

流程框架：
  1、抓取索引页内容
    利用requests请求目标站点，得到索引网页HTML代码，返回结果.
  2、抓取详情页内容
    解析返回结果，得到详情页的链接，并进一步抓取详情页的信息.
  3、下载图片与保存数据库
    将图片下载到本地，并把页面信息及图片URL保存至MongoDB.
  4、开启循环及多线程
    对多页内容遍历，开启多线程提高抓取速度.
"""

import os
import requests
from urllib.parse import urlencode
from hashlib import md5
from multiprocessing.pool import Pool

GROUP_START = 1
GROUP_END = 1


# 加载单个 Ajax 请求结果，将唯一变化的 offset作为参数传递
def get_page(offset):
    params = {      # 请求对的参数
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
    }
    # urlencode（）可以把字典类型转成url参数
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        print("请求索引页出错")
        return None


# 图片链接，并生成构造器,返回一个字典
def get_images(json):
    data = json.get('data')  # 判断这里面是有数据的，然后进行遍历
    if data:
        for item in data:
            title = item.get('title')
            image_list = item.get('image_list')
            if image_list:
                for image in image_list:
                    # 生成器
                    yield {  
                        'image': image.get('url'),
                        'title': title
                    }


# 保存图片的方法
# 其中item就是前面get_images()方法返回的一个字典。在该方法中，首先根据item的title
# 来创建文件夹，然后请求这个图片链接，获取图片的二进制数据，以二进制的形式写入文件。
# 图片的名称可以使用其内容的MD5值，这样可以去除重复。相关代码如下：
def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        local_image_url = item.get('image')
        new_image_url = local_image_url.replace('list','large')
        response = requests.get('http:' + new_image_url)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


# 最后，只需要构造一个offset数组，遍历offset，提取图片链接，并将其下载即可：
def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 1 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()

