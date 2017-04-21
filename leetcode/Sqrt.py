#-*- coding:utf-8 -*-
'''
Created on 2017年4月20日

@author: huangjiaxin
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        p = x / 2
        eps = 0.0003
        while abs(p ** 2 - x) > eps:
            p = (p + (x * 1.0 / p)) / 2.0
        return int(p)
    
if __name__ == '__main__':
    x = 1
    print Solution().mySqrt(x)