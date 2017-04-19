#-*- coding:utf-8 -*-
'''
Created on 2017年4月19日

@author: huangjiaxin
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        j = len(nums)
        for num in range(1, j):
            if nums[num] != nums[num-1]:
                i += 1
                nums[i] = nums[num]
        return i + 1
    
if __name__ == '__main__':
    nums = [1, 1]
    print Solution().removeDuplicates(nums)