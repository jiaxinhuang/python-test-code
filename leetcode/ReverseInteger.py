#-*- coding:utf-8 -*-
'''
Created on 2017年4月18日

@author: huangjiaxin
'''
import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        rev = 0
        flag = 0
        if x > 0:
            flag = 1
        x = abs(x)
        while x != 0:
            rev = rev * 10 + x % 10
            x = x / 10
        if flag == 0:
            rev = -rev
        if ( rev > (1<<31) or -(1<<31) > rev):
            return 0
        else:
            return rev
    
if __name__ == '__main__':
    print Solution().reverse(-1534236469)