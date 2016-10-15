# -*- coding: utf-8 -*-
'''
Created on 2016年10月6日

@author: huangjiaxin
'''

a_in = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

c_in = '''http://www.pythonchallenge.com/pc/def/map.html'''
b = ''
for i in c_in:
    num_i = ord(i)
    if num_i >= 97 and num_i<=122:
        num_new = ((num_i - 97 +2)%26)+97
        b += chr(num_new)
    else:
        b += i
        
print b