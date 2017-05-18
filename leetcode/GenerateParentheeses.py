#-*- coding:utf-8 -*-
'''
Created on 2017年5月18日

@author: huangjiaxin
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(s, left, right, res=[]):
            if left:
                generate(s+'(', left-1, right)
            if right > left:
                generate(s+')', left, right-1)
            if right == 0:
                res.append(s)
            return res
        return generate('', n, n) 
                
    
    
if __name__ == '__main__':
    print Solution().generateParenthesis(3)