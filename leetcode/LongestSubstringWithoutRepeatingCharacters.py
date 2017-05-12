#-*- coding:utf-8 -*-
'''
Created on 2017年5月12日

@author: huangjiaxin
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLen = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and usedChar[s[i]] >= start:
                start = usedChar[s[i]] + 1
            else:
                maxLen = max(maxLen, i - start + 1)
            usedChar[s[i]] = i
        return maxLen
    
if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring('abcabcbb')
    print Solution().lengthOfLongestSubstring('bbbb')
    print Solution().lengthOfLongestSubstring('pwwkew')