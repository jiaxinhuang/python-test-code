#-*- coding:utf-8 -*-
'''
Created on 2017年5月17日

@author: huangjiaxin
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nts = {'2':['a', 'b', 'c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z'],
               '0':[' ']}
        
        if len(digits) == 0:
            return []
        res = ['']
        for i in digits:
            temp = []
            for ch in nts[i]:
                for pr in res:
                    temp.append(pr+ch)
            res = temp
        return res
    
if __name__ == '__main__':
    digits = ''
    print Solution().letterCombinations(digits)