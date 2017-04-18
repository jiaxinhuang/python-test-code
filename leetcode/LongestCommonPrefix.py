#-*- coding:utf-8 -*-
'''
Created on 2017年4月18日

@author: huangjiaxin
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortStr = min(strs, key=len)
        for i in range(len(shortStr)):
            ch = shortStr[i]
            for stro in strs:
                if stro != shortStr:
                    if stro[i] != ch:
                        return shortStr[:i]
        return shortStr

if __name__ == '__main__':
    strs = ['abcdehj', 'abcdefr', 'abcdehjdef', 'ab']
    print Solution().longestCommonPrefix(strs)