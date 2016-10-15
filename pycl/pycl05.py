# -*- coding: utf-8 -*-
'''
Created on 2016年10月8日

@author: huangjiaxin
'''
import pprint, pickle

banner = open('banner.p', 'r')

data_banner = pickle.load(banner)
pprint.pprint(data_banner)

for i in data_banner:
    print ''.join([x[0] * x[1] for x in i])

banner.close()