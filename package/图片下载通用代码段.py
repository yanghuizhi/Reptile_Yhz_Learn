
# 给出一个图片下载的通用代码片段

import requests

def get_pic_from_url(url):        #从url以二进制的格式下载图片数据

    pic_content = requests.get(url,stream=True).content

    open('filename','wb').write(pic_content)