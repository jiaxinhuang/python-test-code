# -*- coding: utf-8 -*-
'''
Created on 2016年10月10日

@author: huangjiaxin
'''

import Image

im = Image.open('oxygen.png')
str_context = ''
for x in xrange(0,609,7):
    num_str = im.getpixel((x, 43))
    print num_str[0],chr(num_str[0])
    
    
    
print str_context.join([chr(im.getpixel((x,43))[0]) for x in xrange(0, 609, 7)])

s2_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print str_context.join([chr(y) for y in s2_list])