# -*- coding: utf-8 -*-
'''
Created on 2016年10月11日

@author: huangjiaxin
'''

# a='1'
# for i in xrange(33):
#     a_len = len(a)
#     count_i = 1
#     new_a=''
#     for j in xrange(a_len):        
#         if j+1 >= a_len:
#             new_a = new_a+str(count_i)+a[j]
#             break
#         elif a[j]==a[j+1]:
#             count_i +=1
#         else:
#             new_a = new_a+str(count_i)+a[j]
#             count_i = 1
#     print i,len(new_a)
#     a = new_a

import re 
initNum = '1'
for each in range(30):
    initNum = ''.join([str(len(i+j)) + i for i,j in re.findall(r'(\d)(\1*)', initNum)])

print len(initNum)
    
