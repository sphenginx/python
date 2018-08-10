#!/usr/bin/python
# encoding: utf-8
import requests
from lxml import etree


url='http://www.chinanews.com/scroll-news/mil/2017/0110/news.shtml'

def getNewUrlList():
    global url
    header ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}  #  构造浏览器头信息
    response=requests.get(url,headers=header) #  获取数据
    html=response.content.decode("gbk")   #  解码
    selector=etree.HTML(html)
    contents = selector.xpath('//div[@id="content_right"]/div[@class="content_list"]/ul/li[div]')   # 使用xpath语法解析获取数据//表示从根开始查找@后跟相应的html属性
    for eachlink in contents:
        url = eachlink.xpath('div/a/@href')[0] if str(eachlink.xpath('div/a/@href')[0]).__contains__("http") else "http://www.chinanews.com"+eachlink.xpath('div/a/@href')[0]
        title = eachlink.xpath('div/a/text()')[0]
        ptime = eachlink.xpath('div[@class="dd_time"]/text()')[0]
        yield (title,url,ptime)

def getNewContent(urlList):
    for title,url,ptime in urlList:
        response=requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'})
        html=response.content.decode("gbk")
        selector=etree.HTML(html)
        title=selector.xpath("//div[@id='cont_1_1_2']/h1/text()")[0]
        source=selector.xpath("//div[@id='cont_1_1_2']/div[@class='left-time']/div[@class='left-t']/text()")[0]
        content=selector.xpath("//div[@id='cont_1_1_2']/div[@class='left_zw']/p/text()")

        i=0
        resultContent=''
        for item in range(0,content.__len__()):
            resultContent+=content[i]
            i+=1
        yield (title,source,resultContent)

if __name__=="__main__":
   urlList= getNewUrlList()
   result= getNewContent(urlList)
   count = 0;
   for title,source,content in result:
       count += 1
       print(str(count) + u"标题:%s"%title)
       #print(u"来源：%s"%source)
       #print(u"正文:%s"%content)
