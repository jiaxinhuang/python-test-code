#-*- coding:utf-8 -*-
'''
Created on 2017年5月25日

@author: huangjiaxin
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
            
    
if __name__ == '__main__':
    print pow(2, 2)