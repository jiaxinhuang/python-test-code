#-*- coding:utf-8 -*-
'''
Created on 2017年5月18日

@author: huangjiaxin
'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not divisor:
            return -1
        sign = ((dividend >= 0) == (divisor >= 0))
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            temp = 1
            tempdivisor = divisor
            while dividend >= tempdivisor:
                tempdivisor = (divisor << temp)
                if dividend >= tempdivisor:
                    temp += 1
            res += 2 ** (temp - 1)
            dividend -= (tempdivisor >> 1)
        if sign == False:
            res = -res
        return min(max(res, -2147483648), 2147483647)


if __name__ == '__main__':
    print Solution().divide(10, 3)