#-*- coding:utf-8 -*-
'''
Created on 2017年4月20日

@author: huangjiaxin
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        at = int(a, 2)
        bt = int(b, 2)
        sb = bin(at + bt)
        return sb[2:]
    
if __name__ == '__main__':
    a = '11'
    b = '1'
    print Solution().addBinary(a, b)