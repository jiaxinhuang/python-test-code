#-*- coding:utf-8 -*-
'''
Created on 2017年4月17日

@author: huangjiaxin
'''
import httplib
import base64
import re
from pprint import pprint


def getrange(page, base, limit):
    conn = httplib.HTTPConnection('www.pythonchallenge.com')
    headers = {'Authorization':'Basic ' + base64.b64encode('butter:fly'),
               'Range':'bytes=%s-%s' % (base, limit)}
    conn.request('GET', page, '', headers)
    return conn.getresponse()

def nextrange(base, bases, results):
    r = getrange('/pc/hex/unreal.jpg', base, 2123456789)
    bases.append(base)
    results.append(r.read())
    try:
        m = re.match('bytes %d-([0-9]+)/2123456789' % base, r.getheader('content-range'))
        return int(m.group(1)) + 1
    except:
        return 'ERR'
    
def moveForward():
    bases = []
    results = []
    b = 30203
    while True:
        b = nextrange(b, bases, results)
        if b == 'ERR':
            break
    pprint(results)
    pprint(bases)

def solve():
    moveForward()
    r = getrange('/pc/hex/unreal.jpg', 2123456789, '')
    msg = r.read()
    print msg
    print msg[::-1]
    print 'invader'[::-1]
    pprint(r.getheaders())
    print getrange('/pc/hex/unreal.jpg', 2123456789, '').read()
    data = getrange('/pc/hex/unreal.jpg', 1152983631, '').read()
    open('unreal.zip', 'wb').write(data)
    
if __name__ == '__main__':
    solve()