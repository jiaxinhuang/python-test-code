# -*- coding: utf-8 -*-
'''
Created on 2016年10月11日

@author: huangjiaxin
'''

import bz2

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

un_de = bz2.decompress(un)
pw_de = bz2.decompress(pw)

print "the decompress username:",un_de
print "the decompress pwd:",pw_de