# -*- coding: utf-8 -*-
'''
Created on 2016年10月15日

@author: huangjiaxin
'''

import datetime
import calendar

for year in xrange(1006, 2000, 10):
    if datetime.date(year, 1, 27).weekday() == 1 and calendar.isleap(year):
        print year,datetime.date(year, 1, 27).isoformat()