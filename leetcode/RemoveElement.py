#-*- coding:utf-8 -*-
'''
Created on 2017年4月19日

@author: huangjiaxin
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        newlen = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[newlen] = nums[i]
                newlen += 1
        return newlen
    
if __name__ == '__main__':
    nums = [4,4,0,1,0,2]
    val = 0
    print Solution().removeElement(nums, val)