# -*- coding: utf-8 -*-
'''
Created on 2016年10月12日

@author: huangjiaxin
'''

import Image

im = Image.open('cave.jpg')
im_w, im_h = im.size
# print im_w, im_h

images = [Image.new(im.mode, (im_w/2, im_h/2)) for num in xrange(4)]
images_load = [i.load() for i in images]
org = im.load() #take the value of every point

for j in xrange(im_w):
    for k in xrange(im_h):
        org_pos = (j, k)
        new_pos = (j / 2, k / 2)
        images_load[j%2+k%2*2][new_pos] = org[org_pos]
        
[images[l].save('%d.png' % l) for l in xrange(4)]