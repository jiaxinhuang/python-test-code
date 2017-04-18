#-*- coding:utf-8 -*-
'''
Created on 2017年4月18日

@author: huangjiaxin
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            a = nums[i]
            for j in range(i+1, len(nums)):
                b = nums[j]
                if a + b == target:
                    return [i, j]
                
if __name__ == '__main__':
    a = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print a.twoSum(nums, target)