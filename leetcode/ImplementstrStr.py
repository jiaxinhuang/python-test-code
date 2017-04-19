#-*- coding:utf-8 -*-
'''
Created on 2017年4月19日

@author: huangjiaxin
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hlen, nlen = len(haystack), len(needle)
        if nlen == 0:
            return 0
        if hlen == 0 or hlen < nlen:
            return -1
        for i in range(hlen - nlen + 1):
            if haystack[i:i+nlen] == needle:
                return i
        return -1


if __name__ == '__main__':
    haystack = ''
    needle = ''
    print Solution().strStr(haystack, needle)
    
