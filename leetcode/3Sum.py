#-*- coding:utf-8 -*-
'''
Created on 2017年5月16日

@author: huangjiaxin
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        else:
            nums.sort()
            res = set()
            for i in range(len(nums) - 2):
                if i >= 1 and nums[i] == nums[i - 1]:
                    continue
                d = {}
                for x in nums[i+1:]:
                    if x not in d:
                        d[-nums[i] - x] = 1
                    else:
                        res.add((nums[i], -nums[i]-x, x))
        return map(list, res)
            
                
if __name__ == '__main__':
    S = [-1, 0, 1, 2, -1, -4]
    print Solution().threeSum(S)