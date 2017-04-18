#-*- coding:utf-8 -*-
'''
Created on 2017年4月18日

@author: huangjiaxin
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if (x < 0 or x % 10 == 0):
            return False
        temp = 0
        while x > temp:
            temp = temp * 10 + x % 10
            x = x / 10
        if (x == temp or temp / 10 == x):
            return True
        else:
            return False

if __name__ == '__main__':
    print Solution().isPalindrome(0)