#-*- coding:utf-8 -*-
'''
Created on 2017年5月9日

@author: huangjiaxin
'''
import urllib
import bz2

def main():
    html = urllib.urlopen('http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html').read()
    html = html.split('\n')[12:]
    data = [chr(len(i)) for i in html]
    print bz2.decompress(''.join(data))
    
if __name__ == '__main__':
    main()