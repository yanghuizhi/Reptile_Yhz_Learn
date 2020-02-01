#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""

Created on Sat Jun  9 06:12:38 2018

@author: wupeng

"""

import requests

import time

from bs4 import BeautifulSoup

import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'}

csv_house_list = []

for i in range(1, 2):

    link = 'https://guangzhou.anjuke.com/sale/dongchuan/p' + str(i) + r'/#filtersort'

    r = requests.get(link, headers=headers, timeout=20)

    soup = BeautifulSoup(r.text, 'lxml')

    house_list = soup.find_all('li', class_="list-item")

    for house in house_list:
        housename = house.find('div', class_="house-title").a.string.strip()

        totalprice = house.find('span', class_="price-det").get_text()

        unitprice = house.find('span', class_="unit-price").get_text()

        noofroom = house.find('div', class_="details-item").span.string.strip()

        housearea = house.find('div', class_="details-item").contents[3].string.strip()

        housefloor = house.find('div', class_="details-item").contents[5].string.strip()

        houseyear = house.find('div', class_="details-item").contents[7].string.strip()

        housebroker = house.find('span', class_="brokername").get_text()

        housebroker = housebroker.replace('\ue147', '')

        houseaddress = house.find('span', class_="comm-address").get_text()

        houseaddress = houseaddress.replace('\xa0', '')

        houseaddress = houseaddress.replace('\n', '')

        houseaddress = houseaddress.replace('  ', '')

        housetaglist = house.find_all('span', class_='item-tags')

        housetags = [i.get_text() for i in housetaglist]

        dic = {'house_name': housename, 'total_price': totalprice, 'unit_price': unitprice, 'no_of_rooms': noofroom,
               'house_area': housearea, 'house_floor': housefloor, 'hourse_year': houseyear,
               'house_broker': housebroker, 'house_address': houseaddress, 'hourse_tag': housetags}

        print(dic)

        csv_house_list.append(dic)

    time.sleep(5)

    print('page' + str(i))

df = pd.DataFrame(csv_house_list)

print(df)

df.to_csv("安居客房价收集日志.txt", encoding="utf-16", sep="\t")
