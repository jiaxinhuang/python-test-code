#-*- coding:utf-8 -*-
'''
Created on 2017年5月25日

@author: huangjiaxin
'''
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
    
if __name__ == '__main__':
    nums = [1]
    print Solution().permuteUnique(nums)