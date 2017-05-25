#-*- coding:utf-8 -*-
'''
Created on 2017年5月25日

@author: huangjiaxin
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in xrange(len(perm)+1):
                    new_perms.append(perm[:i]+[n]+perm[i:])
            perms = new_perms
            print perms
        return perms
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)


if __name__ == '__main__':
    nums = [1,2,3]
    print Solution().permute(nums)