# -*- coding:utf-8 -*-
'''
Created on 2016年11月8日
作为对糗事百科网页内容的爬取
步骤：
1、获取网页源代码
2、对源代码做正则匹配
3、将获取到的信息格式化输出
4、将获取到的数据写入data.txt文件中

说明：由于只是出于测试目的，只爬了一页内容，由于此网站URL规则普通，只需修改page的值即可获取多页内容
@author: huangjiaxin
'''
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib
import urllib2
import re

page = 1
url = "http://www.qiushibaike.com/8hr/page/"+str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
headers = {'User-Agent' : user_agent}
try:
    request = urllib2.Request(url, headers= headers)
    response = urllib2.urlopen(request)
    print response 
except urllib2.URLError,e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

content = response.read().decode('utf-8')
# print content
#做正则匹配，需要根据网页的改变而修改
pattern = re.compile('<div.*?author clearfix">.*?<img.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?class="stats-vote">.*?class="number">(.*?)</i>.*?class="number">(.*?)</i>',re.S)

print "doing match"
items = re.findall(pattern, content)

print "show items"
file = open("data.txt","w")
for item in items:
    print item[0],item[1],item[2],item[3]
    text = str(item[0])+str(item[1])+str(item[2])+str(item[3])
    file.write(text)
    
file.close()