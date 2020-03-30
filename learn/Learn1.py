# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

# 请求方式罗列
r1 = requests.get('https://www.baidu.com/')
r2 = requests.post('http://httpbin.org/post')
r3 = requests.put('http://httpbin.org/put')
r4 = requests.delete('http://httpbin.org/delete')
r5 = requests.head('http://httpbin.org/get')
r6 = requests.options('http://httpbin.org/get')

# 类型————————————————————————————————————
print(type(r1))        # 类型
print(type(r1.text))   # 返回 str 类型
print(type(r2.json))   # 返回 method 类型

# 打印数据并解决乱码问题————————————————————————————
print(r1.text)  # 打印网页信息,可能会出现乱码,怎么办？
print(r1.encoding)  # 返回当前编码格式
r1.encoding = 'utf-8'  # 转换编码
print(r1.text)  # 再次打印

print(r2.json())  # 打印 json 数据，有可能会报错哦
# print(json.loads(r1.text.txt))  # 解析json 数据
# print(type(r1.json()))  # 查看类型 dict

print(r1.content)  # 乱码怎么办？返回二进制格式
print(r1.content.decode("utf-8"))  # 转换编码,再次打印解决

# 一些方法——————————————————————————————————
print(r1.status_code)  # 返回状态码
print(r1.url)  # 返回网页的URL，可以查看插入的data、params数据
print(r1.history)  # 请求历史，不是太会用
print(r1.headers)  # 响应头
print(r1.cookies)  # 返回的浏览器缓存




"""
当使用json格式报错时，如下解决
    a. 针对字符串来进行处理，保证字符串符合json的格式要求
    b.  借助第三方包的帮助顺利解决这个问题（更好点）

         我们这里使用了demjson的包来处理这个问题。
         安装： pip install demjson
         使用：  json_obj = demjson(json_string)
         快速说明： http://deron.meranda.us/python/demjson/  
         demjson有两个主要的方法：
         encode  编码，将对象转换为json
         decode   解码，将json转化为对象
总结
    这个问题的产生主要还是服务端在进行json转换的过程中没有很好处理好这个问题造
成的，正常来说，一般不应该出现的的。
"""