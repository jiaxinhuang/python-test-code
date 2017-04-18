#-*- coding:utf-8 -*-
'''
Created on 2017年4月18日

@author: huangjiaxin
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        if len(s) == 1:
            return num[s]
        pre = 0
        index = len(s) - 1
        while(index >= 0):
            curInt = num[s[index]]
            if curInt >= pre:
                sum += curInt
            else:
                sum -= curInt
            pre = curInt
            index -= 1
        return sum
        
if __name__ == '__main__':
    print Solution().romanToInt('XCIX')