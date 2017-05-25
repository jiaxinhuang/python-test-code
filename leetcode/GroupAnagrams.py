#-*- coding:utf-8 -*-
'''
Created on 2017年5月25日

@author: huangjiaxin
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        res = []
        for i, str in enumerate(strs):
            str = ''.join((lambda x:(x.sort(), x)[1])(list(str)))
            if str not in m:
                m[str] = [i]
            else:
                m[str].append(i)
        
        for key in m:
            temp = []
            for i in m[key]:
                temp.append(strs[i])
            res.append(temp)
        return res 
        
if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print Solution().groupAnagrams(strs)