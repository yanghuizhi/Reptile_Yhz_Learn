# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/2/18 11:11 上午
import time

from selenium import webdriver

url='https://music.163.com/'
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)
browser = webdriver.Chrome()

while url != 'javacript:void(0)':
    browser.get(url)
    time.sleep(2)
    browser.switch_to.frame('')
    data=browser.find_element_by_id('').find_elements_by_tag_name('')

    # for i in range(len(data)):
    for i in range(10):
        num=data[i].find_element_by_class_name('nb').text
        if '万' in num and int(num.split('万')[0])>1000:
            msk = data[i].find_element_by_css_selector('')
            with open('163playlist.txt','a') as f:
                f.write([ 'msk.title', 'msk.num','msk.href'])
    url=browser.find_element_by_css_selector('').get_attribute('')

browser.close()