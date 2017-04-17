#-*- coding:utf-8 -*-
'''
Created on 2017年4月13日

@author: huangjiaxin
'''
import urllib
import urllib2
import cookielib
import re
import bz2
import xmlrpclib

def getcookie1():
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.HTTPHandler)
    f = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php')
    html = f.read()
    for cookie in cj:
        print cookie
    
    pat = re.compile('and the next busynothing is (\d+)')
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
    nextnum = '12345'
    cookies = []
    while True:
        f = opener.open(url+str(nextnum))
        html = f.read()
        for cookie in cj:
            cookies.append(cookie)
        matchRes = pat.findall(html)
        if matchRes:
            nextnum = matchRes[0]
            print nextnum
        else:
            break
    print cookies

    values = [x.value for x in cookies]
    msg = urllib.unquote_plus("".join(values))
    print bz2.decompress(msg)

    proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print proxy.phone('Leopold')
    list(cj)[0].value = 'the+flowers+are+on+their+way'
    print opener.open('http://www.pythonchallenge.com/pc/stuff/violin.php').read()
    
if __name__ == '__main__':
    getcookie1()
