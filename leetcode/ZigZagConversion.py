#-*- coding:utf-8 -*-
'''
Created on 2017年5月15日

@author: huangjiaxin
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s
        else:
            sorts = [[] for x in range(numRows)]
            step = 1
            lang = 0
            for ch in s:
                sorts[lang].append(ch)
                if lang == 0:
                    step = 1
                elif lang == numRows - 1:
                    step = -1
                lang += step
        return ''.join(''.join(row) for row in sorts)
    
if __name__ == '__main__':
    print Solution().convert('PAYPALISHIRING', 3)