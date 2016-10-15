# -*- coding: utf-8 -*-
'''
Created on 2016年10月12日

@author: huangjiaxin
'''

f = open('evil2.gfx', 'rb')
content = f.read()
f.close()

for i in xrange(5):
    f = open('%d' % i, 'wb')
    f.write(content[i::5])
    f.close()