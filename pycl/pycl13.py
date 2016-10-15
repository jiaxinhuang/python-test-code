# -*- coding: utf-8 -*-
'''
Created on 2016年10月13日

@author: huangjiaxin
'''
import xmlrpclib

evil = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print evil.system.listMethods()
print evil.system.methodHelp('phone')
print evil.phone('Bert')