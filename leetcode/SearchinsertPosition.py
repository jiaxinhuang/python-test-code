#-*- coding:utf-8 -*-s
'''
Created on 2017年4月19日

@author: huangjiaxin
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums and target:
            return 0
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                return i


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 3
    print Solution().searchInsert(nums, target)