#! /usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json


# 封装好函数，只需要传入url即可

def Post_Request(url, headers, data=None, json=None, verify=False):
    response = requests.post(url=url, headers=headers, data=data, json=json, verify=verify)
    # verify=False 可以跳过SSL的证书验证
    try:
        if response.status_code == 200:
            # print("转换编码为：", response.content.decode("utf-8"))
            # print("text输出：",response.text )  # 可能会导致乱码
            # print("content输出：",response.content )  # 可以更换此方式
            print(response.text)
        else:
            raise ValueError("status_code is:", response.status_code)
    except requests.ConnectionError:
        print("请求索引页出错")

    return None


def Get_Request1(url, headers, data):
    response = requests.get(url=url, headers=headers, data=data, verify=False).json()

    if response.status_code == 200:
        return json.dumps(response, indent=2, sort_keys=False)
    else:
        print('请求失败,状态码为{response.status_code}')

    return None


def Get_Request2(url, headers, data):
    response = requests.get(url=url, headers=headers, data=data, verify=False).content

    if response.status_code == 200:
        return json.loads(response.decode('utf-8'), indent=2, sort_keys=False)
    else:
        print('请求失败,状态码为{response.status_code}')

    return None
