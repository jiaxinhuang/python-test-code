#-*- coding:utf-8 -*-
'''
Created on 2017年5月22日

@author: huangjiaxin
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        def search(left, right):
            if nums[left] == target and nums[right] == target:
                return [left, right]
            elif nums[left] <= target and nums[right] >= target:
                mid = (left + right) / 2
                l, r = search(left, mid), search(mid+1, right)
                if -1 in l+r:
                    return max(l, r)
                else:
                    return [l[0], r[1]]
            return [-1, -1]
        return search(0, len(nums)-1)
    

if __name__ == '__main__':
    S = [5, 7, 7, 8, 8, 10]
    target = 8
    print Solution().searchRange(S, target)
            