#-*- coding:utf-8 -*-
'''
Created on 2017年4月21日

@author: huangjiaxin
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        tem = [1,2]
        if n < 3:
            return tem[n-1]
        for i in range(2, n):
            tem.append(tem[i - 1] + tem[i - 2])
        return tem[-1]

if __name__ == '__main__':
    n = 35
    print Solution().climbStairs(n)