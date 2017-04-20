#-*- coding:utf-8 -*-
'''
Created on 2017年4月19日

@author: huangjiaxin
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        if n == 1:
            return s
        for i in range(n-1):
            num = 1
            snew = ''
            for ch in range(len(s)):
                if ch+1 == len(s):
                    snew = snew + str(num) + s[ch]
                else:
                    if s[ch] != s[ch+1]:
                        snew = snew + str(num) + s[ch]
                        num = 1
                    else:
                        num += 1
            s = snew
        return s
    
if __name__ == '__main__':
    n = 2
    print Solution().countAndSay(n)