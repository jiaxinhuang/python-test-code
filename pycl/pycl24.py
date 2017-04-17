#-*- coding:utf-8 -*-
'''
Created on 2017年4月17日

@author: huangjiaxin
'''
import this
import string

def main():
    msg = 'va gur snpr bs jung'
    frm = string.ascii_lowercase
    to = string.ascii_lowercase[13:] + string.ascii_lowercase[0:13]
    table = string.maketrans(frm, to)
    print msg.translate(table)
    
if __name__ == '__main__':
    main()