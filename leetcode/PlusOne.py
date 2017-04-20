#-*- coding:utf-8 -*-
'''
Created on 2017年4月20日

@author: huangjiaxin
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        L = len(digits)
        for i in range(L):
            num = num + digits[i] * pow(10, L - i - 1)
        return [int(i) for i in str(num+1)]
    

if __name__ == '__main__':
    digits = [1, 2, 3, 4]
    print Solution().plusOne(digits)