#-*- coding:utf-8 -*-
'''
Created on 2017年5月16日

@author: huangjiaxin
'''
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0:
            return 0
        tmp ='0'
        result = 0
        i = 0
        if str[0] in '+-':
            tmp = str[0]
            i = 1
        MAX = 2147483647
        MIN = -2147483648
        for i in range(i, len(str)):
            if str[i].isdigit():
                tmp += str[i]
            else:
                break
        if len(tmp) > 1:
            temp = int(tmp)
            if temp > MAX:
                result = MAX
            elif temp < MIN:
                result = MIN
            else:
                result = temp
        return result
    
if __name__ == '__main__':
    print Solution().myAtoi('-0012a42')
            