# -*- coding: utf-8 -*-
'''
Created on 2016年10月15日

@author: huangjiaxin
'''

import Image

im = Image.open('mozart.gif')
print im.size
w, h = im.size
value_im = im.load()

for i in xrange(w):
    print [value_im[i, j] for j in xrange(h)]