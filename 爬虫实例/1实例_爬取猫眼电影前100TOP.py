# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    爬取猫眼TOP100的电影信息
    反思：通过正则我实现了爬取电影信息，但提取页面信息时使用的是正则表达式，这还是比较烦琐，
而且万一有地方写错了，可能导致匹配失败，所以使用正则表达式提取页面信息多多少少还是有些不方便。
对于网页的节点来说，它可以定义id、class或其他属性。而且节点之间还有层次关系，在网页中可以通过XPath
或CSS选择器来定位一个或多个节点。那么，在页面解析时，利用XPath或CSS选择器来提取某个节点，然后再调用相应
方法获取它的正文内容或者属性，不就可以提取我们想要的任意信息了吗？
    那我们怎么实现呢？其中比较强大的库有lxml、Beautiful Soup、pyquery等，通过对这些库的学习，我们就不用
再为正则表达式发愁，而且解析效率也会大大提高。

流程框架：
  1、抓取单页内容
    利用requests请求目标站点，得到单个网页html代码，返回结果
  2、正则表达式分析
    根据html代码分析得到电影的名称、主演、上映时间、评分、图片链接等信息
  3、保存至文件
    通过文件的形式将结果保存，每一部电影一个结果一行json字符串
  4、开启循环及多线程
    对多页内容遍历，开启多线程提高抓取速度
"""

import json
import requests
from requests.exceptions import RequestException
import re
import time
# from multiprocessing import Pool    # 多进程，进程池


# 首先抓取第一页内容，并传入url，并返回结果，在通过 man（）调用
# 最后的结果就是，获取一个html的返回
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/65.0.3325.162 Safari/537.36 '
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:   # 通过状态码来判断犯返回结果
            return response.text
        return None
    except RequestException:
        return None


# 通过正则表达式来从结果中提取出我们想要的内容，解析网页
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)  # re.S匹配换行符，这个最好有，完善代码
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


# 写入文件，指定ensure_ascii参数为False，这样可以保证输出结果是中文形式而不是Unicode编码。
# content 此时就是一个字典
def write_to_file(content):
    with open('猫眼电影前100日志.txt', 'a', encoding='utf-8') as f:
        # json.dumps ,将字典转化成字符串
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


# 通过上面3步，最后汇总到这里，结束
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


# 实现分页爬取，
if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)

    # pool = Pool()  #声明一个进程池
    # 将数组中每个元素当成函数的参数创建一个个进程放到进程池去运行
    # 第二个参数构造一个数组
    # 不到一秒就抓取了下来，上面的那个方法最少10秒
    # pool.map(main,[i*10 for i in range(10)])  
   