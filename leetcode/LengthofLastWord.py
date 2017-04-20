#-*- coding:utf-8 -*-
'''
Created on 2017年4月20日

@author: huangjiaxin
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        sList = s.strip().split()
        if len(sList) <= 0:
            return 0
        L = len(sList[-1])
        return L
    
if __name__ == '__main__':
    s = "        "
    print Solution().lengthOfLastWord(s)