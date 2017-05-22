#-*- coding:utf-8 -*-
'''
Created on 2017年5月19日

@author: huangjiaxin
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        L = len(nums)
        for i in range(L-1, 0, -1):
            if nums[i] > nums[i-1]:
                break
        if nums[i] > nums[i-1]:
            tempVal = nums[i-1]
            tempState = i-1
            for j in range(i, L):
                if nums[j] <= tempVal:
                    break
            print j
            if j == L-1 and nums[j] > tempVal:
                nums[tempState] = nums[j]
                nums[j] = tempVal
            else:
                nums[tempState] = nums[j-1]
                nums[j-1] = tempVal
            
            tempNums = nums[tempState+1:L]
            tempNums.sort()
            for i in range(len(tempNums)):
                nums[tempState+1+i] = tempNums[i]
        else:
            nums.sort()
        return

if __name__ == '__main__':
    S1 = [2,2,7,5,4,3,2,2,1]
    S2 = [1,3,2]
    Solution().nextPermutation(S1)
    print S1