import requests
path = "/Users/yhz/Desktop/" #设置图片文件路径，前提是必须要有abc这个文件夹
url = 'https://mmbiz.qpic.cn/mmbiz_png/WwPkUCFX4x47ONgVzpiahxAiaicpsoBjyWckjxIzFFd0OYVsx7QTvhp1K9GI5GUbZJR5A8LbVVB5V0RMMXdAEiaFCg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1'
r = requests.request('get',url) #获取网页
print(r.status_code)
with open(path,'wb') as f:  #打开写入到path路径里-二进制文件，返回的句柄名为f
    f.write(r.content)  #往f里写入r对象的二进制文件
f.close()