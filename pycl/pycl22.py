#-*- coding:utf-8 -*-
'''
Created on 2017年4月17日

@author: huangjiaxin
'''
import bz2
import zlib
from pprint import pprint

def uncompress(data, logs):
    if data[:2] == 'x\x9c':
        logs.append('*')
        return zlib.decompress(data)
    elif data[:2] == 'BZ':
        logs.append('#')
        return bz2.BZ2Decompressor().decompress(data)
    elif data[-2:] == '\x9cx':
        logs.append('@')
        return zlib.decompress(data[::-1])
    elif data[-2:] == 'ZB':
        logs.append('$')
        return bz2.BZ2Decompressor().decompress(data[::-1])
    else:
        raise ValueError
    

def solve():
    data = open('package.pack').read()
    logs = []
    while True:
        try:
            data = uncompress(data, logs)
        except:
            print "Decompress ends!"
            break
    logs.pop(0)
    print data
    pprint(''.join(logs).replace('*', ' ').split('@'))


if __name__ == '__main__':
    solve()