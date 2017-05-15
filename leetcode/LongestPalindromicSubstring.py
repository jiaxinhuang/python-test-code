#-*- coding:utf-8 -*-
'''
Created on 2017年5月12日

@author: huangjiaxin
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            res = max(self.withmiddle(s, i, i), self.withmiddle(s, i, i+1), res, key=len)
        return res
        
    def withmiddle(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
if __name__ == '__main__':
    s = 'abbaddddd'
    print Solution().longestPalindrome(s)