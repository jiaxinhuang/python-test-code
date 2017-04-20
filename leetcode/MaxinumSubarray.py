#-*- coding:utf-8 -*-
'''
Created on 2017年4月20日

@author: huangjiaxin
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxsum = nums[0]
        Sum = 0
        for i in range(len(nums)):
            if Sum < 0:
                Sum = 0
            Sum += nums[i]
            maxsum = max(Sum, maxsum)
        return maxsum
    
if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print Solution().maxSubArray(nums)