#-*- coding:utf-8 -*-
'''
Created on 2017年5月24日

@author: huangjiaxin
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        L1 = len(num1)
        L2 = len(num2)
        temp = [0 for i in range(L1+L2-1)]
        for i in range(L1):
            for j in range(L2):
                temp[i+j] += int(num1[i])*int(num2[j])
        res = ''
        d = 0
        for k in range(len(temp)-1, 0, -1):
            num = temp[k] + d
            res = str(num % 10) + res
            d = num / 10
        return str(temp[0]+d)+res


if __name__ == '__main__':
    num1 = '9133'
    num2 = '0'
    print Solution().multiply(num1, num2)