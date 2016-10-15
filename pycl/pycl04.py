# -*- coding: utf-8 -*-
'''
Created on 2016年10月7日

@author: huangjiaxin
'''

import urllib2

url_first = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
url_part = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

url_use = url_first
for n in xrange(400):
    request = urllib2.Request(url_use)
    response = urllib2.urlopen(request)

    a = response.read()

    num = ''
    for i in a:
        if i.isdigit():
            num +=i
    if num == '':
        print a
        num=raw_input("num: ")
        
    if len(num) >7:
        print a
        num=raw_input("num: ")
    
    print n,num
    url_use = url_part + str(num)
        

# print response.read()