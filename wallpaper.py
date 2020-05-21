# -*-coding:utf-8 -*-
# python 3.6+

import re
import urllib.request
import chardet


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    encode_type = chardet.detect(html)  
    html = html.decode(encode_type['encoding'])
    return html


def saveImages(imglist):
    success_num = 0
    fail_num = 0
    for imageURL in imglist:
        splitPath = imageURL.split('/')
        fileName = splitPath.pop()
        # 对于每张图片地址，进行保存
        try:
            u = urllib.request.urlretrieve(imageURL, 'wallpaper\\' + fileName) #需要提前要创建文件夹
            print('downloading:' + fileName)
            success_num += 1
        except:
            print('error:' + fileName)
            fileName += 1
            pass

    print("success_num：" + str(success_num) + ', fail_num：' + str(fail_num))


def getAllImg(html):
    #利用正则表达式把源代码中的图片地址过滤出来
    # reg = r'src="(https://.+?\.jpg)"'
    # reg = r'data-actualsrc="(.*?)">'
    reg = r'data-actualsrc="(https?://pic.+?\.jpg|png|jpeg)"'
    imgre = re.compile(reg, re.S)
    imglist = imgre.findall(html) #表示在整个网页中过滤出所有图片的地址，放在imglist中
    return imglist


if __name__ == '__main__':
    html = getHtml("https://www.zhihu.com/question/309298287/answer/583183127")
    imglist = getAllImg(html) #获取图片的地址列表
    saveImages(imglist) # 保存图片