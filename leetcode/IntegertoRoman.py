#-*- coding:utf-8 -*-
'''
Created on 2017年5月16日

@author: huangjiaxin
'''
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rn = ''
        sr = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        sn = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4,1]
        i = 0
        while num > 0:
            rn += ((num // sn[i])*sr[i])
            num = num % sn[i]
            i += 1
        return rn 